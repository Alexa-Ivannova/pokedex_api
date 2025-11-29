# CONTROLADORES:
from src.controllers.pokemon_controller.create_pokemon_controller import create_pokemon
from src.controllers.pokemon_controller.get_all_pokemon_controller import get_all_pokemon
from src.controllers.pokemon_controller.get_pokemon_by_id_controller import get_pokemon_by_id
from src.controllers.pokemon_controller.update_pokemon_controller import update_pokemon
from src.controllers.pokemon_controller.delete_pokemon_controller import delete_pokemon


def register_pokemon_routes(app):
    # ENDPOINT GET_ALL PARA TRAER TODOS LOS ENTRENADORES
    @app.route("/pokemon", methods = ["GET"])
    def get_all_pokemon_route():
        return get_all_pokemon()

    # ENDPOINT GET_ID PARA TRAER UN ENTRENADOR POR ID
    @app.route("/pokemon/id/<int:id>", methods = ["GET"])
    def get_pokemon_by_id_route(id):
        return get_pokemon_by_id(id)


    # ENDPOINT CREAR POKEMON
    @app.route("/pokemon", methods = ["POST"])
    def create_pokemon_route():
        return create_pokemon()
    
    # ENDPOINT ACTUALIZAR ENTRENADOR
    @app.route("/pokemon/id/<int:id>", methods = ["PATCH"])
    def update_pokemon_route(id):
        return update_pokemon(id)

    #ENDPOINT ELIMINAR ENTRENADOR
    @app.route("/pokemon/id/<int:id>", methods = ["DELETE"])
    def delete_pokemon_route(id):
        return delete_pokemon(id)
