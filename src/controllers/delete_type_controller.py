from flask import jsonify
from src.db import get_db
from src.controllers.get_type_by_id_controller import specific_type

def delete_type(id):
    try:
        response_id, status_id= specific_type(id)
        if status_id not in (200, 201):
            return jsonify({
                "status": 400,
                "message": "Id not found"
            }), 400
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""UPDATE types SET deleted_at = now()
                    where id = %s;
                    """,(id,))
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({
            "status": 200,
            "message": "Type deleted successfully"
        }), 200

    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500