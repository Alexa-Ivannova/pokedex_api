from flask import jsonify

# SERVICIOS:
from src.services.capture_service import capture_service

def get_all_captures():
    try: 
        
        data_get_all_captures = capture_service.get_all_captures()

        response = []

        for data in data_get_all_captures:
            print("data for:", data)
            response.append({
                "id_captures": data[0],
                "name_trainer":  data[1],
                "name_pokemon": data[2],
                "level_pokemon": data[3],
                "name_type": data[4],
                "captura_date": data[5]
            })

        return jsonify({
            "status": 200,
            "message": "Route get all successfully",
            "data": response
        }), 200

    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500