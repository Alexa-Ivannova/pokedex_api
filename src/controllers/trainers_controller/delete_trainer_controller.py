from flask import jsonify,request

# SERVICIOS:
from src.services.trainer_services import trainer_service

def delete_trainer(id):
    try: 
        
        # VALIDATE IF ID EXIST:
        search_id = trainer_service.get_by_id(id)

        if not search_id:
            return jsonify({
                "status": 400,
                "message": "Id not found"
            }), 400
        
        trainer_service.delete_trainer(id)

        return jsonify({
            "status": 200,
            "message": "The trainer was deleted successfully"
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500
