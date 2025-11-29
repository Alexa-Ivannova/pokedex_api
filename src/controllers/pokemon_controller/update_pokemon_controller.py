from flask import jsonify, request

# SERVICIOS
from src.services.pokemon_services import pokemon_service

def update_pokemon(id):
    try:
        data_body = request.get_json()

        search_pokemon_id = pokemon_service.get_pokemon_by_id(id)

        if not search_pokemon_id:
            return jsonify({
                "status": 400,
                "message": "Pokemon not found"
            })
        
        data_pokemon = {
            "id": id,
            "name": data_body.get("name"),
            "level": data_body.get("level"),
            "type_id": data_body.get("type_id")
        }

        data_update = pokemon_service.update_pokemon(data_pokemon)

        data_return = {
            "id": id,
            "name": data_update[1],
            "level": data_update[2],
            "type_id": data_update[3]
        }

        return jsonify({
            "status": 200,
            "message": "Route update all successfully",
            "data": data_return
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }),500