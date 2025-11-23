from flask import jsonify, request
from src.db import get_db
from src.controllers.get_type_by_id_controller import specific_type

# SERVICIOS:
from src.services.type_services import type_service


def update_type(id):
    try:
        response_id, status_id=  specific_type(id)
        if status_id not in (200, 201):

            return jsonify({
                "status": 400,
                "message": "Id not found"
            }),400

        data_body = request.get_json()
        name_type = data_body.get("name_type")

        type_service.update(name_type, id)

        return jsonify({
            "status": 200,
            "message": "The type was updated successfully"          
        }),200
        
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500