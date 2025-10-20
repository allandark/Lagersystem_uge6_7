from flask_restx import Namespace, Resource
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from models import get_user_model, get_login_model


jwt = JWTManager()

authorizations = {
    "jsonWebToken":{
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}


auth_ns = Namespace("auth", description="User namespace", authorizations=authorizations)
user_model = get_user_model(auth_ns)
login_model = get_login_model(auth_ns)

test_users = []

test_data = {
    "key1": 1,
    "key2": "value"
}


@auth_ns.route('/')
@auth_ns.route('/login')
class Login(Resource):
    ''' Login to user
    '''
    @auth_ns.doc('Login to user')
    @auth_ns.expect(login_model)    
    def post(self):
        user = None
        for u in test_users:
            if u["username"] == auth_ns.payload["username"]:
                user = u
        
        if not user:
            return {"error": "User does not exists"}, 401
        if not check_password_hash(user["password_hash"],auth_ns.payload["password"]):
            return {"error": "Incorrect password"}, 401
        return {"access_token": create_access_token(user["username"])}

@auth_ns.route('/register')
class Register(Resource):
    ''' Register user
    '''
    @auth_ns.doc('Register user')
    @auth_ns.expect(login_model)
    @auth_ns.marshal_with(user_model)
    def post(self):
        user = {
            "id": len(test_users),
            "username": auth_ns.payload["username"],
            "password_hash": generate_password_hash(auth_ns.payload["password"])
        }
        test_users.append(user)
        return {"id": user["id"], "name": user["username"]}, 201



@auth_ns.route('/tests')
class Test(Resource):
    ''' Test endpoint
    '''

    method_decorators = [jwt_required()]    
    @auth_ns.doc('Test endpoint',security="jsonWebToken")
    def get(self):
        return test_data

