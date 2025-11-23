from flask import jsonify

# SERVICIOS:
from src.services.trainer_services import trainer_service

def get_all_trainers():
    try:
        
        data = trainer_service.get_all()

        if not data:
            return jsonify({
                "status": 404,
                "Message": "Trainers not found"
            }), 404


        get_all_return = []


        for row in data:
            get_all_return.append({
                "id": row[0],
                "name": row[1].upper(),
                "region": row[2]
            })

        return jsonify({
            "status": 200,
            "message": "Route get all successfully",
            "data": get_all_return
        })
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500
    