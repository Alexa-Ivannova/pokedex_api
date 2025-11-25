# IMPORTAR DEPENDENCIAS
from flask import request, jsonify
from marshmallow import ValidationError

# IMPORTAR ESQUEMAS
from src.schemas.trainers.trainers_schemas import TrainerSchema

# IMPORTAR SERVICIO
from src.services.trainer_services import trainer_service

def create_trainer():
    trainer_schema = TrainerSchema()
    data_body = request.get_json()

    # TRY PARA VALIDACIÓN DE SISTEMA
    try:
        data_cleaned = trainer_schema.load(data_body)
    
    except ValidationError as err:
        return jsonify({
            "status": 400,
            "message": "Validation error",
            "fields": err.messages
        }), 400
    
    #TRY PARA LOGICA DEL NEGOCIO
    try:
        # DATA LIMPIA
        id_cleaned = data_cleaned.get("id")
        name_cleaned = data_cleaned.get("name")
        region_cleaned = data_cleaned.get("region")

        # VALIDAR DATA
        if not id_cleaned and not name_cleaned and not region_cleaned:
            return jsonify({
                "staus": 400,
                "Message": "Data body has required :D"
            }), 400
        
        data = {
            "id": id_cleaned,
            "name": name_cleaned,
            "region": region_cleaned
        }

        # ENVIAR DATA CREADA A LA BASE DE DATOS
        trainer_created = trainer_service.create_trainer(data)

        response = {
            "id": trainer_created,
            "name": name_cleaned,
            "region": region_cleaned
        }
        

        return jsonify({
            "status": 201,
            "message": "Create route is successfully",
            "data": response
        }), 201


    except Exception as e:
        print(e)
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500