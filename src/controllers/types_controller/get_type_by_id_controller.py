from flask import jsonify

# SERVICIOS:
from src.services.type_services import Type_service

def specific_type(id):
    try:

        data_db = Type_service.get_by_id(id)

        if not data_db or data_db [4]!= None:
            return jsonify({
                "status": 400,
                "message": "id not found"
            }), 400
        
        return jsonify({
            "status": 200,
            "message": "Specific type retrieved successfully",
            "data": data_db
        }),200
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }),500