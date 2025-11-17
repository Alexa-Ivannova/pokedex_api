from flask import jsonify
from src.db import get_db

def specific_type(id):
    try:
        
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""SELECT * FROM types
                    WHERE id = %s;""",(id,))
        type_found = cur.fetchone()
        print(type_found)
        cur.close()
        conn.close()

        if not type_found or type_found[4]!= None:
            return jsonify({
                "status": 400,
                "message": "id not found"
            }), 400
        
        return jsonify({
            "status": 200,
            "message": "Specific type retrieved successfully",
            "data": type_found
        }),200
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }),500