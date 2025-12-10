from functools import wraps
from flask import request, jsonify
import os

def api_required():
    def _api_required(fn):
        @wraps(fn)
        def __api_required(*args, **kwargs):
            API_KEY = os.getenv("API_KEY")

            key = request.headers.get("key-auth")
            if not key:
                return jsonify({
                    "status": 400,
                    "message": "Authorization is required"
                }), 400
            
            if key != API_KEY:
                return jsonify({
                    "status": 401,
                    "message": "Unauthorized"
                }), 401

            return fn(*args, **kwargs)
        return __api_required
    return _api_required

