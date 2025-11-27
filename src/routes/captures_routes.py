# CONTROLADORES
from src.controllers.capture_controller.create_capture_controller import create_capture


def register_captures_routes(app):

    # ENDPOINT GET_ALL PARA TRAER TODAS LAS CAPTURAS

    # ENDPOINT GET_ID PARA TRAER UNA CAPTURA POR ID    

    # ENDPOINT CREAR CAPTURA 
    @app.route("/capture", methods = ["POST"])
    def create_capture_route():
        return create_capture()

    # ENDPOINT ACTUALIZAR CAPTURA

    #ENDPOINT ELIMINAR CAPTURA

