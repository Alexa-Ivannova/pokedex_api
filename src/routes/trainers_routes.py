from src.controllers.trainers_controller.create_trainer_controller import create_trainer

def register_trainer_routes(app):
    @app.route("/trainer", methods = ["POST"] )
    def create_trainer_route():
        return create_trainer()
