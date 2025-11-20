# IMPORTAR DEPENDENCIAS:
from flask import request, jsonify
from src.services.type_services import type_service
from marshmallow import ValidationError

# IMPORTAS ESQUEMAS
from src.schemas.types.types_schemas import validate_type_payload, TypeSchema
def create_type():
    type_schema = TypeSchema()
    data_body = request.get_json()

    # TRY PARA VALIDAR ERRORES EN DATA
    try:
        data_cleaned = type_schema.load(data_body)
        
    except ValidationError as err:
        return jsonify({
            "status": 400,
            "message": "Validation error",
            "fields": err.messages
        }), 400


    try:
        
        # errors = validate_type_payload(data_body)
        # if errors:
        #     return jsonify({
        #         "status": 400,
        #         "message": "Validation error",
        #         "fields": errors
        #     }), 400

        name_type = data_cleaned.get("name_type")
        description = data_cleaned.get("description")

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