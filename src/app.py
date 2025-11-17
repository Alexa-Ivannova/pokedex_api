# FLASK: Framework de python que permite facilitar el montaje del backend:
# 1) Importar dependencias para poder usarlas 
from flask import Flask
from dotenv import load_dotenv
from src.routes.types_routes import register_type_routs
from src.db import get_db

# 2) inicializar servidor--> crear variable app 
# Instanciar = llamar la clase ... atributo = caracteristica ... metodos = acciones 
app = Flask(__name__)
load_dotenv()

register_type_routs(app)

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

# Encender servidor: escribir igual:
if __name__ == "__main__":
    app.run(debug=True)