from functools import wraps
from flask import request, jsonify
from marshmallow import Schema, fields, validate, ValidationError

# ESQUEMA VANILLA 
def validate_type_payload(data):
    errors = {}
    if "name_type" not in data or not isinstance(data["name_type"],str) or not data["name_type"].strip():
        errors["name_type"]="String required"
    
    if "description" in data and data["description"] is not None and not isinstance(data["description"], str):
        errors["description"]="Must be string or null"

    return errors

# ESQUEMA CON DECORADOR
def validate_type_payload_schema():
    def _validate_type_payload_schema(fn):
        @wraps(fn)
        def wrapper(*arg, **kwargs):
            data = request.get_json()
            errors = {}
            if "name_type" not in data or not isinstance(data["name_type"],str) or not data["name_type"].strip():
                errors["name_type"]="String required"
    
            if "description" in data and data["description"] is not None and not isinstance(data["description"], str):
                errors["description"]="Must be string or null"
            
            if errors:
                return jsonify({
                    "status": 400,
                    "message": "Validation error",
                    "fields": errors
                }), 400
            
            return data
        return wrapper
    return _validate_type_payload_schema


# ESQUEMA CON MARSHMALLOW NORMAL
class TypeSchema(Schema):
    name_type = fields.Str(required=True, validate=validate.Length(min=4, max=15))
    description = fields.Str(allow_none=True)

# ESQUEMA CON MARSHMALLOW CON DECORADOR