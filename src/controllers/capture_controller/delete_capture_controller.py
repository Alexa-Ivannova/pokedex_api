from flask import jsonify

# SERVICIOS
from src.services.capture_service import capture_service

def delete_capture(id):
    try:

        search_id_capture = capture_service.get_capture_by_id(id)
        if not search_id_capture:
            return jsonify({
                "status": 400,
                "message": "Capture not found"
            }), 400
        
        delete_capture_id = capture_service.delete_capture(id)

        return jsonify({
            "status": 200,
            "message": "Create route is successfully"
        }), 200
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500