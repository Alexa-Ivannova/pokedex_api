from flask import jsonify

# SERVICIO:
from src.services.pokemon_services import pokemon_service

def get_pokemon_by_id(id):
    try:
        
        data_pokemon_id = pokemon_service.get_pokemon_by_id(id)

        if not data_pokemon_id:
            return jsonify({
                "status": 404,
                "message": "Pokemon not found" 
            }), 404
        
        data_return = {
            "id": data_pokemon_id[0],
            "name": data_pokemon_id[1],
            "level": data_pokemon_id[2],
            "type_id": data_pokemon_id[3]
        }

        return jsonify({
            "status": 200,
            "message": "Route get by id successfully",
            "data": data_return
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500