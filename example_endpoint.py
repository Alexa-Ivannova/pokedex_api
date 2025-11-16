# 3) Crear ruta (.route) con un endpoint ("/helath)") y un metodo (methods= [GET]) el @ es un decorador--> Identifica la función decoradora que envuelve otra función
# 4) Crear función q retorna jsonify
@app.route("/health", methods = ["GET"])
def health():
    return jsonify(
        {
            "status": 200,
            "message": "ok",
            "service": "Pokedex"
        }
    ), 200

# Recibir un pokemon -- De acuerdo al pokemon devolver el tipo de ataque que hace y el daño que hace --
# Endpoint Pokemon

@app.route("/pokemon", methods = ["POST"])
def pokemon():

    # Capturar datos desde el body del cliente 
    data_body = request.get_json()
    name_pokemon = data_body.get("name_pokemon").capitalize()

    # Listado de pokemones
    pokemones = {
        "Charmander": {
            "tipo": "Fuego",
            "daño": 50
        },

        "Gengar": {
            "tipo": "Fantasma",
            "daño": 45
        },

        "Eve": {
            "tipo": "Gay",
            "daño": 20
        }
    }

    # Captura error si no hay body:
    if not data_body:
        return jsonify({
            "status": 400,
            "message": f"El body se encuentra vacio",
            "service": "Pokedex"
        }), 400

    # Captura error si el dato es != de string
    if not isinstance(name_pokemon, str):
        return jsonify({
            "status": 400,
            "message": f"El valor ingresado {name_pokemon} debe ser un texto",
            "service": "Pokedex"
        }), 400

    # Captura error si el pokemon NO existe
    if name_pokemon not in pokemones:
        return jsonify({
            "status": 404,
            "message": f"El pokemon {name_pokemon} no fue encontrado",
            "service": "Pokedex"
        }), 404
    
    # De acuerdo al pokemon devolver el tipo de ataque que hace y el daño que hace
    # Logica para devolver la data de acuerdo al pokemon seleccionado
    for key_pokemon, values in pokemones.items():
        if name_pokemon == key_pokemon:
            result = (f"El pokemon es {name_pokemon} su tipo es {values["tipo"]} y el daño que hace es {values["daño"]}")

    # Respuesta satisfactoria del endpoint
    return jsonify({
        "status": 200,
        "message": "Ok",
        "service": "Pokedex",
        "data": result
        }), 200
