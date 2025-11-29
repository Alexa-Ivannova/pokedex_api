# FLASK: Framework de python que permite facilitar el montaje del backend:
# 1) Importar dependencias para poder usarlas 
from flask import Flask
from dotenv import load_dotenv
from src.models.main_model import(pokemon_db,trainers_db,types_db,captures_db)
from src.routes.main_routes import (register_trainer_routes, register_type_routs, register_pokemon_routes, register_captures_routes)


# Instanciar = llamar la clase ... atributo = caracteristica ... metodos = acciones 
app = Flask(__name__)
load_dotenv()

# Registrar las rutas 
register_type_routs(app)
register_trainer_routes(app)
register_pokemon_routes(app)
register_captures_routes(app)

# Modelo (tabla) types 
types_db()
trainers_db()
pokemon_db()
captures_db()

# Encender servidor: escribir igual:
if __name__ == "__main__":
    app.run(debug=True)