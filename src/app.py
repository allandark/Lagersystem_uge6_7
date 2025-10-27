from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from apis import create_api, jwt
from database_commands.database_manager import DatabaseManager
from database_commands.product import ProductModel
from core.config import Config, ReadConfigFile




def create_app():
    # Create App
    config = ReadConfigFile("config.json")

    dbManger = DatabaseManager(
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

    api = create_api(
        title="Lagersystem API",
        version="1.0",
        description="Largersystem API",
        swagger_ui=config.swagger_ui,
        db_manager=dbManger
    )
    # Init endpoints
    api.init_app(app,docs=config.swagger_ui)

    # json webtoken manager
    jwt.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(
        host=app.config["API_HOST"],
        port=app.config["API_PORT"],
        debug=app.config["DEBUG"])
    