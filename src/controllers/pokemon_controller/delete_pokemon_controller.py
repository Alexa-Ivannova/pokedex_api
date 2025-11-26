from flask import jsonify

#SERVICIOS:
from src.services.pokemon_services import pokemon_service

def delete_pokemon(id):
    try: 

        search_id = pokemon_service.get_pokemon_by_id(id)

        if not search_id:
            return jsonify({
                "status": 400,
                "messaje": "Id not found"
            })
        
        delete_pokemon_id = pokemon_service.delete_pokemon(id)

        return jsonify({
            "status": 200,
            "message": "Route delete successfully"
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500