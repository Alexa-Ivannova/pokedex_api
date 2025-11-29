from flask import jsonify, request

# SERVICIOS
from src.services.pokemon_services import pokemon_service
from src.services.type_services import type_service

def create_pokemon():
    try:
        data_body = request.get_json()

        if not data_body:
            return jsonify({
                "status": 400,
                "message": "Data body is empty"
            }),400
        
        name = data_body.get("name")
        level = data_body.get("level")
        type_id = data_body.get("type_id")

        if not type_id:
            return jsonify({
                "status": 400,
                "message": "Type Id is missing in request"
            }),400
        
        
        name_pokemon = pokemon_service.get_pokemon_by_name({"name": name})
        print("Nombre pokemon",name_pokemon)

        if name_pokemon: 
            search_pokemon_name = name_pokemon[1]
                
            if name == search_pokemon_name:
                return jsonify({
                    "status": 400,
                    "message": "Pokemon is already exist"
                }),400
        
        type_pokemon = type_service.get_by_id(type_id)


        if not type_pokemon:
            return jsonify({
                "status": 400,
                "message": "Type id not found"
            }), 400
        

        data = {
            "name": name,
            "level": level,
            "type_id": type_id
        }

        pokemon_created = pokemon_service.create_pokemon(data)

        data.update({
            "id": pokemon_created
        })

        return jsonify({
            "status": 201,
            "message": "Create pokemon is successfully",
            "data": data
        }), 201
    
    except Exception as e:
        return jsonify({
            "status": 500,
            "error": str(e)
        }), 500