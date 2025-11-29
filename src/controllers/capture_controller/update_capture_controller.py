from flask import jsonify, request

# SERVICIOS
from src.services.capture_service import capture_service
from src.services.trainer_services import trainer_service
from src.services.pokemon_services import pokemon_service


def update_capture(id):
    try:
        data_body = request.get_json()

        # VALIDAR SI EXISTE EL ID INGRESADO
        search_id_capture = capture_service.get_capture_by_id(id)

        if not search_id_capture:
            return jsonify({
                "status": 404,
                "message": "Capture not found"
            }), 404
        
        data_capture = {
            "id": id,
            "trainer_id": data_body.get("trainer_id"),
            "pokemon_id": data_body.get("pokemon_id"),
            "capturated_at": data_body.get("capturated_at")
        }

        trainer_id = data_body.get("trainer_id")
        pokemon_id = data_body.get("pokemon_id")

        search_trainer = trainer_service.get_by_id(trainer_id)
        if not search_trainer:
            return jsonify({
                "status": 400,
                "mesage": "Trainer not found"
            }), 400
        
        search_pokemon = pokemon_service.get_pokemon_by_id(pokemon_id)
        if not search_pokemon:
            return jsonify({
                "status": 400,
                "mesage": "Pokemon not found"
            }), 400

        data_update = capture_service.update_capture(data_capture)
        
        search_capture_update = capture_service.get_capture_by_id(id)

        response = {
            "id": id,
            "trainer_id": search_capture_update[1],
            "pokemon_id": search_capture_update[2],
            "capturated_at": search_capture_update[3]
        }

        return jsonify({
            "status": 200,
            "message": "Route",
            "data": response
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500