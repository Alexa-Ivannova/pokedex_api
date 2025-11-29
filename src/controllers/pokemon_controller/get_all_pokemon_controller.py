from flask import jsonify

# SERVICIOS:
from src.services.pokemon_services import pokemon_service

def get_all_pokemon():
    try:

        data_all_pokemon = pokemon_service.get_all_pokemon()

        if not data_all_pokemon:
            return jsonify({
                "status": 400,
                "message": "Data Pokemon not found"
            }), 400

        data_return = []

        for pokemon in data_all_pokemon:
            data_return.append({
                "id": pokemon[0],
                "name": pokemon[1],
                "level": pokemon[2],
                "type_id": pokemon[3]
            })
                
        return jsonify({
            "status": 200,
            "message": "Route get all successfully",
            "data": data_return
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500