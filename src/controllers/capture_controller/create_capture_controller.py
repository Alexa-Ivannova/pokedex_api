from flask import jsonify, request

# SERVICIOS
from src.services.trainer_services import trainer_service
from src.services.pokemon_services import pokemon_service
from src.services.capture_service import capture_service

def create_capture():
    try:

        data_body = request.get_json()

        # VALIDACION SI NO EXISTE NADA EN DATA:
        if not data_body:
            return jsonify({
                "status": 400,
                "message": "Data not found"
            }), 400
        
        # VALIDACIÓN EXISTA ID ENTRENADOS Y ID POKEMON
        trainer_id = data_body.get("trainer_id")
        pokemon_id = data_body.get("pokemon_id")

        if not trainer_id or not pokemon_id:
            return jsonify({
                "status": 400,
                "message": "trainer id and pokemon id is required"
            }), 400
        

        # VALIDACIÓN EXISTEN LOS ID INGRESADOS POR EL CLIENTE
        search_trainer_id = trainer_service.get_by_id(trainer_id)
        search_pokemon_id = pokemon_service.get_pokemon_by_id(pokemon_id)

        if not search_pokemon_id:
            return jsonify({
                "status": 404,
                "message": "Pokemon not found"
            }), 404
        
        if not search_trainer_id:
            return jsonify({
                "status": 404,
                "message": "Trainer not found"
            }), 404
        
        # TODO PENDIENTE CREAR VALIDACIÓN DE SI YA EXISTE EL ENTRENADOR CON ESE POKEMON NO LO CREE
        # SERVICIO Q LLAME AL ENTRENADOR Y VERIFIQUE SI YA ESTA CREADO CON ESE POKEMON

        capture_pokemon = capture_service.create_capture(data_body)

        print("capture pokemon: ", capture_pokemon)

        # data_body.append(capture_pokemon)
        data_body["id"] = capture_pokemon[0]



        return jsonify({
            "status": 200,
            "message": "Route create succsessfully",
            "data": data_body
        }), 200
    
    except Exception as e:

        return jsonify({
            "status": 500,
            "error": str(e)
        })
    
    

