from flask import jsonify, request

# SERVICIOS:
from src.services.trainer_services import trainer_service

def update_trainer(id):
    try:
        data_body = request.get_json()

        # VALIDATE IF DATABODY EXIST:
        if not data_body:
            return jsonify({
                "status": 400,
                "message": "Fields data body empty"
            }), 400
        
        # VALIDATE IF ID EXIST:
        search_id = trainer_service.get_by_id(id)

        if not search_id:
            return jsonify({
                "status": 400,
                "message": "Id not found"
            }), 400
        
        data = {
            "id": id,
            "name": data_body.get("name"),
            "region": data_body.get("region")
        }


        data_updated = trainer_service.update_trainer(data)
        
        if not data_updated:
            return jsonify({
                "status": 400,
                "message": "Not found"
            })
        

        data_trainer = {
            "id": id,
            "name": data_updated[1],
            "region": data_updated[2]
        }
    
        return jsonify({
            "service": 200,
            "message": "The type was updated successfully",
            "data": data_trainer
        }), 200
    

    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500