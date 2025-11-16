# FLASK: Framework de python que permite facilitar el montaje del backend:
# 1) Importar dependencias para poder usarlas 
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import psycopg2 
import psycopg2.extras 
import os

# 2) inicializar servidor--> crear variable app 
# Instanciar = llamar la clase ... atributo = caracteristica ... metodos = acciones 
app = Flask(__name__)
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL").strip()
print("Valor data base",repr(DATABASE_URL))

# ABRIR UNA CONECCIÓN EN LA BD
def get_db():
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def init_db():
    try: 
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS types (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) UNIQUE NOT NULL,
                    description TEXT,
                    created_at TIMESTAMP DEFAULT NOW()
                    );
                    """)
        conn.commit()
        cur.close()
        conn.close()
        print("TABLA TIPOS CREADA OK")
    except Exception as e:
        print("Error al iniciar la BD", e)
    # finally:
    #     if conn:
    #         conn.close()

init_db()

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

# Encender servidor: escribir igual:
if __name__ == "__main__":
    app.run(debug=True)


