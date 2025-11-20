import time
from flask import request, jsonify
from functools import wraps

def route_guard(label):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.time()

            try:
                resp = fn(*args, **kwargs)
                duration = round((time.time() - start)*1000,2)
                print(f"[{label}], OK {request.method} {request.path} {duration} ms")
                return resp

            except Exception as e:
                duration = round((time.time() - start)*1000,2)
                print(f"[{label}], OK {request.method} {request.path} {duration} ms -> {e}")
                return jsonify({
                    "status": 500,
                    "error": "Error interno"
                }), 500
        return wrapper
    return decorator
