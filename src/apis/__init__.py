from flask_restx import Api

from apis.auth import api as auth_ns
from apis.auth import jwt
from apis.products import api as product_ns
from apis.warehouse import api as warehouse_ns


# TODO: make configurable
api = Api(
    title="Lagersystem API",
    version="1.0",
    description="Largersystem API",
    doc="/docs"  # Swagger UI endpoint
)

api.add_namespace(auth_ns)
api.add_namespace(product_ns)
api.add_namespace(warehouse_ns)
# Add more endpoints here