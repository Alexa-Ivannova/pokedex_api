# CONTROLADORES:
from src.controllers.pokemon_controller.create_pokemon_controller import create_pokemon


def register_pokemon_routes(app):
    # ENDPOINT CREAR POKEMON
    @app.route("/pokemon", methods = ["POST"])
    def create_pokemon_route():
        return create_pokemon()
    