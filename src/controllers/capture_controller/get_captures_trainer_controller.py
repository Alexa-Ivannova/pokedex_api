from flask import jsonify

# SERVICIOS
from src.services.trainer_services import trainer_service
from src.services.capture_service import capture_service

def get_captures_trainer(trainer_id):
    try:

        search_id_trainer = trainer_service.get_by_id(trainer_id)
        id_trainer = search_id_trainer[0]

        if not search_id_trainer:
            return jsonify({
                "status": 404,
                "message": "Trainer not found"
            }), 404 

        search_captures_trainer = capture_service.get_by_trainer_id_capture(id_trainer)

        response = []

        for capture in search_captures_trainer:
            print("captura:", capture)
            response.append({
                "id_capture": capture[1],
                "trainer_name": capture[2],
                "pokemon_name": capture[3],
                "pokemon_level": capture[4],
                "pokemon_type": capture[5],
                "capture_date": capture[6]
            })

        return jsonify({
            "status": 200,
            "messgage": "Route get all successfully",
            "data": response
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500