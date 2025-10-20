from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
from auth_controller import auth_ns, jwt

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

# TODO: Move to safe config file
app.config["JWT_SECRET_KEY"] = "this is a secret"

api = Api(
    title="Lagersystem API",
    version="1.0",
    description="Largersystem API",
    doc="/docs"  # Swagger UI endpoint
)

api.init_app(app)
jwt.init_app(app)
api.add_namespace(auth_ns)


if __name__ == '__main__':
    app.run(debug=True)