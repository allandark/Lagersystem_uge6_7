from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from apis import api, jwt

# Create App
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

# TODO: Move to safe config file
app.config["JWT_SECRET_KEY"] = "this is a secret"

# Init endpoints
api.init_app(app)

# json webtoken manager
jwt.init_app(app)


app.run(debug=True)