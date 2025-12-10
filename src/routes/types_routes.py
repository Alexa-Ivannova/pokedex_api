# IMPRTAR CONTROLADORES:
from src.controllers.types_controller.create_type_controller import create_type
from src.controllers.types_controller.list_types_controller import list_types
from src.controllers.types_controller.get_type_by_id_controller import specific_type
from src.controllers.types_controller.update_type_controller import update_type
from src.controllers.types_controller.delete_type_controller import delete_type

# DECORADORES:
from src.utils.route_guard_decorator import route_guard
from src.controllers.auth.auth_controller import api_required

# SCHEMAS
from src.schemas.types.types_schemas import validate_type_payload_schema

def register_type_routs(app):
    # ENDPOINT CREAR TABLA TYPES        
    @app.route("/types", methods = ["POST"])
    # ESQUEMA MANUAL:
    # @validate_type_payload_schema()
    def create_type_route():
        return create_type()
        
    # ENDPOINT TRAER LISTADO DE TODOS LOS TIPOS QUE HAY EN LA TABLA
    @app.route("/types", methods = ["GET"])
    @route_guard("Hola, a mimir") 
    def list_type_route():
        return list_types()

    # END POINT PARA TRAER UN TIPO DE POKEMON ESPECIFICO
    @app.route("/type/update/id/<int:id>", methods =["GET"])
    def get_type_by_id_route(id):
        return specific_type(id)
    
    # ENDPOINT PARA MODIFICAR UN DATO ESPECIFICO (PATCH)
    @app.route("/update/<int:id>", methods = ["PATCH"])
    @api_required()
    @route_guard("Modificar dato especifico")
    def update_type_route(id):
        return update_type(id)
    
    # ENDPOINT PARA ELIMINAR (DELETE SOFT)
    @app.route("/delete/<int:id>", methods = ["DELETE"])
    @api_required()
    def delete_type_route(id):
        return delete_type(id)