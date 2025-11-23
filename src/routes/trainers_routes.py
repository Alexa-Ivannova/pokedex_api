# CONTROLADOR:
from src.controllers.trainers_controller.create_trainer_controller import create_trainer
from src.controllers.trainers_controller.get_all_trainers_controller import get_all_trainers



def register_trainer_routes(app):

    # ENDPOINT CREAR ENTRENADOR
    @app.route("/trainer", methods = ["POST"] )
    def create_trainer_route():
        return create_trainer()

    # METODO GET_ALL
    @app.route("/trainers", methods = ["GET"])
    def get_all_trainers_route():
        return get_all_trainers()
