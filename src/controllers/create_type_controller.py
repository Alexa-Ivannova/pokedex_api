# IMPORTAR DEPENDENCIAS:
from flask import request, jsonify
from src.services.type_services import type_service

def create_type():
    try:
        data_body = request.get_json()
        
        name_type = data_body.get("name_type")
        description = data_body.get("description")

        if not name_type:
            return jsonify({
                "status": 400,
                "message": "Name is required"
            }), 400
        
        if not isinstance(name_type, str):
            return jsonify({
                "status": 400,
                "message": "The name type must be str"
            }), 400
        
        type_created = type_service.create(name_type, description)

        data_response = {
            "name": name_type,
            "description": description,
            "id": type_created
        }

        return jsonify({
            "status": 201,
            "message": "Created type successfully",
            "data": data_response
        }), 201

    except Exception as e:
        print(e)
        return jsonify({
            "status": 500,
            "error": str(e)
        }
        ), 500