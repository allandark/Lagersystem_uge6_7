from flask_restx import Api
from apis.auth import create_api_auth, jwt
from apis.products import create_api_product
from apis.warehouse import create_api_warehouse
from apis.customer import create_api_customer



def create_api(
    title: str, 
    version: str, 
    description: str, 
    swagger_ui: bool,
    db_manager):

    use_swagger = "/docs" if swagger_ui else False
    api = Api(
        title= "Lagersystem API",
        version= "1.0",
        description= "Largersystem API",
        doc= use_swagger
    )

    api.add_namespace(create_api_auth(db_manager))
    api.add_namespace(create_api_product(db_manager))
    api.add_namespace(create_api_warehouse(db_manager))
    api.add_namespace(create_api_customer(db_manager))
    # Add more endpoints here

    return api
