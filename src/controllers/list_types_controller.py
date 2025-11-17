from src.db import get_db
from flask import jsonify

def list_types():
    try:

        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM types ORDER BY id;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        
        types = {}
        for row in rows:
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