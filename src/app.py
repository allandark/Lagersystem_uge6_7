from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from apis import api, jwt
from database_commands.database_mangment import Database_mangment
from database_commands.product import ProductModel
from core.config import Config, ReadConfigFile




def create_app():
    # Create App
    config = ReadConfigFile("config.json")

    dbManger = Database_mangment(
        host = config.db_host, 
        user = config.db_user, 
        password= config.db_password,
        dbname= config.db_name)
    
    
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    app.config["JWT_SECRET_KEY"] = config.jwt_token
    app.config["DEBUG"] = config.debug
    app.config["SWAGGER_UI"] = config.swagger_ui
    app.config["API_HOST"] = config.api_host
    app.config["API_PORT"] = config.api_port
    # Init endpoints
    api.init_app(app,docs=config.swagger_ui) # does not set the swagger ui correctly

    # json webtoken manager
    jwt.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host=app.config["API_HOST"],
        port=app.config["API_PORT"],
        debug=app.config["DEBUG"])
    