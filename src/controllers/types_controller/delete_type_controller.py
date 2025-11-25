from flask import jsonify
from src.controllers.types_controller.get_type_by_id_controller import specific_type
from src.services.type_services import type_service

def delete_type(id):
    try:
        response_id, status_id= specific_type(id)
        if status_id not in (200, 201):
            return jsonify({
                "status": 400,
                "message": "Id not found"
            }), 400
        
        type_deleted = type_service.delete(id)
        if type_deleted != True:
            return jsonify({
                "status": 444,
                "message": "Id wasn´t possible delete"
            }),444

        return jsonify({
            "status": 200,
            "message": "Type deleted successfully"
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500