# CONTROLADOR:
from src.controllers.trainers_controller.create_trainer_controller import create_trainer
from src.controllers.trainers_controller.get_all_trainers_controller import get_all_trainers
from src.controllers.trainers_controller.get_trainer_by_id_controller import get_trainer_by_id
from src.controllers.trainers_controller.update_trainer_controller import update_trainer
from src.controllers.trainers_controller.delete_trainer_controller import delete_trainer

# MIDELWARE
from src.controllers.auth.auth_controller import api_required


def register_trainer_routes(app):

    # ENDPOINT GET_ALL PARA TRAER TODOS LOS ENTRENADORES
    @app.route("/trainers", methods = ["GET"])
    def get_all_trainers_route():
        return get_all_trainers()
    
    # ENDPOINT GET_ID PARA TRAER UN ENTRENADOR POR ID
    @app.route("/trainer/id/<string:id>", methods = ["GET"])
    def get_by_id_route(id):
        return get_trainer_by_id(id)

    # ENDPOINT CREAR ENTRENADOR
    @app.route("/trainer", methods = ["POST"] )
    @api_required()
    def create_trainer_route():
        return create_trainer()
    
    # ENDPOINT ACTUALIZAR ENTRENADOR
    @app.route("/trainer/update/<string:id>", methods = ["PATCH"])
    @api_required()
    def update_trainer_route(id):
        return update_trainer(id)
    
    #ENDPOINT ELIMINAR ENTRENADOR
    @app.route("/trainer/delete/<string:id>", methods = ["DELETE"])
    @api_required()
    def delete_trainer_route(id):
        return delete_trainer(id)