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

        print("Pokemon id:", search_pokemon_id)

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
        
        name_trainer = search_trainer_id[1]
        name_pokemon = search_pokemon_id[1]
        
        #VALIDACIÓN DE SI YA EXISTE EL ENTRENADOR CON ESE POKEMON NO LO CREE
        capture_match_trainer_and_pokemon = capture_service.get_match_trainer_and_pokemon_capture(data_body)

        if capture_match_trainer_and_pokemon:
            return jsonify({
                "status": 400,
                "message": "Capture exists"
            }), 400

        # CREAR CAPTURA
        capture_pokemon = capture_service.create_capture(data_body)

        response = {
            "name_pokemon": name_pokemon,
            "name_trainer": name_trainer
        }

        return jsonify({
            "status": 200,
            "message": "Route create succsessfully",
            "data": response
        }), 200
    
    except Exception as e:

        return jsonify({
            "status": 500,
            "error": str(e)
        })
    
    

