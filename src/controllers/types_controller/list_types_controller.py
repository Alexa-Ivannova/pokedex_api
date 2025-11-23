from src.db import get_db
from flask import jsonify

# SERVICIOS:
from src.services.type_services import type_service

def list_types():
    try:
        data_db = type_service.get_all()
        
        types = {}
        for row in data_db:
            if row[4]!= None:
                continue
                
            types[row[1]]={
                "id": row[0],
                "name": row[1],
                "description": row[2],
                "created_at": row[3]
            }

        return jsonify ({
            "status": 200,
            "message": "List type retrieved successfully",
            "data": types
        }), 200
    
    except Exception as e:
        print(e)
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500