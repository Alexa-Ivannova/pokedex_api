from flask import jsonify

# CONTROLADORES:
from src.controllers.create_type_controller import create_type
from src.controllers.list_types_controller import list_types
from src.controllers.get_type_by_id_controller import specific_type
from src.controllers.update_type_controller import update_type
from src.controllers.delete_type_controller import delete_type

def register_type_routs(app):
    @app.route("/types", methods = ["POST"])
    def create_type_route():
        return create_type()
    
    # ENDPOINT TRAER LISTADO DE TODOS LOS TIPOS QUE HAY EN LA TABLA
    @app.route("/types", methods = ["GET"])
    def list_type_route():
        return list_types()
    
    # END POINT PARA TRAER UN TIPO DE POKEMON ESPECIFICO
    @app.route("/type/id/<int:id>", methods =["GET"])
    def get_type_by_id_route(id):
        return specific_type(id)
    
    # ENDPOINT PARA MODIFICAR UN DATO ESPECIFICO (PATCH)
    @app.route("/update/<int:id>", methods = ["PATCH"])
    def update_type_route(id):
        return update_type(id)
    
    # ENDPOINT PARA ELIMINAR (DELETE SOFT)
    @app.route("/delete/<int:id>", methods = ["DELETE"])
    def delete_type_route(id):
        return delete_type(id)