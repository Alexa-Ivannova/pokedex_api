# FLASK: Framework de python que permite facilitar el montaje del backend:
# 1) Importar dependencias para poder usarlas 
from flask import Flask
from dotenv import load_dotenv
from src.routes.types_routes import register_type_routs
from src.models.types_model import types_db

# Instanciar = llamar la clase ... atributo = caracteristica ... metodos = acciones 
app = Flask(__name__)
load_dotenv()

# Registrar las rutas 
register_type_routs(app)

# Modelo (tabla) types 
types_db()

# Encender servidor: escribir igual:
if __name__ == "__main__":
    app.run(debug=True)