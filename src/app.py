from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from apis import api, jwt
from Database_commands.database_mangment import Database_mangment





def create_app():
    # Create App
    dbManger = Database_mangment(host = "localhost", user = "root", password="",dbName="lagersystem")
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)

    # TODO: Move to safe config file
    app.config["JWT_SECRET_KEY"] = "this is a secret"

    # Init endpoints
    api.init_app(app)

    # json webtoken manager
    jwt.init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)