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
DATABASE_URL = os.getenv("DATABASE_URL")

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

    except Exception as e:
        print("Error al iniciar la BD", e)

init_db()

# CREAR ENDPOINT (@app.route("apunte_a_la_ruta", methods = ["INGRESE METODO A USAR"]))
@app.route("/types", methods = ["POST"])
def create_type():
    try:
        data_body = request.get_json()
        
        name_type = data_body.get("name_type")
        description = data_body.get("description")

        if not name_type:
            return jsonify({
                "status": 400,
                "message": "Name is required"
            }), 400
        
        if not isinstance(name_type, str):
            return jsonify({
                "status": 400,
                "message": "The name type must be str"
            }), 400
        
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
                    INSERT INTO types(name, description)
                    VALUES (%s,%s) RETURNING id;
                    """, (name_type, description))
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        data_response = {
            "name": name_type,
            "description": description,
            "id": new_id
        }

        return jsonify({
            "status": 201,
            "message": "Created type successfully",
            "data": data_response
        }), 201

    except Exception as e:
        print(e)
        return jsonify({
            "status": 500,
            "error": str(e)
        }
        ), 500


# Encender servidor: escribir igual:
if __name__ == "__main__":
    app.run(debug=True)

