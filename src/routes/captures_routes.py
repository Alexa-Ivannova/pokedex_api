# CONTROLADORES
from src.controllers.capture_controller.create_capture_controller import create_capture
from src.controllers.capture_controller.get_all_captures_controller import get_all_captures
from src.controllers.capture_controller.get_captures_trainer_controller import get_captures_trainer
from src.controllers.capture_controller.get_capture_pokemon_controller import get_capture_pokemon
from src.controllers.capture_controller.update_capture_controller import update_capture
from src.controllers.capture_controller.delete_capture_controller import delete_capture


def register_captures_routes(app):

    # ENDPOINT GET_ALL PARA TRAER TODAS LAS CAPTURAS
    @app.route("/captures", methods = ["GET"])
    def get_all_captures_route():
        return get_all_captures()

    # ENDPOINT PARA TRAER CAPTURAS DEL ENTRENADOR 
    @app.route("/capture/id/<string:id>", methods = ["GET"])
    def get_captures_trainer_route(id):
        return get_captures_trainer(id)
    
    # ENDPOINT PARA TRAER CAPTURAS DEL POKEMON
    @app.route("/capture/id/pokemon/<string:id>", methods = ["GET"])
    def get_capture_pokemon_route(id):
        return get_capture_pokemon(id)

    # ENDPOINT CREAR CAPTURA 
    @app.route("/capture", methods = ["POST"])
    def create_capture_route():
        return create_capture()

    # ENDPOINT ACTUALIZAR CAPTURA
    @app.route("/capture/<int:id>", methods = ["PATCH"])
    def update_capture_route(id):
        return update_capture(id)

    #ENDPOINT ELIMINAR CAPTURA
    @app.route("/capture/<int:id>", methods = ["DELETE"])
    def delete_capture_route(id):
        return delete_capture(id)

