from flask import jsonify
# SERVICIOS
from src.services.capture_service import capture_service
from src.services.pokemon_services import pokemon_service


def get_capture_pokemon(id_pokemon):
    try:

        search_id_pokemon = pokemon_service.get_pokemon_by_id(id_pokemon)

        if not search_id_pokemon:
            return jsonify({
                "status": 404,
                "message": "Pokemon not found"
            })

        search_captures_pokemon_id = capture_service.get_by_pokemon_id_capture(id_pokemon)

        response = []

        for capture in search_captures_pokemon_id:
            print("capture", capture)
            response.append({
                "id_captura": capture[0],
                "pokemon_name": capture[2],
                "trainer_name": capture[3],
                "pokemon_type": capture[4],
                "pokemon_level": capture[5],
                "capture_date": capture[6]
            })

        return jsonify({
            "status": 200,
            "message": "Create route is successfully",
            "data": response
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500