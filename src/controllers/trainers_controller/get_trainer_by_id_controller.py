from flask import jsonify

# SERVICIOS 
from src.services.trainer_services import trainer_service

def get_trainer_by_id(id):
    try:

        data = trainer_service.get_by_id(id)

        if not data:
            return jsonify({
                "status": 404,
                "Message": "Trainers not found"
            }), 404
        
        get_data_id_return = {
                "id": data[0],
                "name": data[1],
                "region": data[2]
            }

        return jsonify({
            "status": 200,
            "message": "Route get id successfully",
            "data": get_data_id_return
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500