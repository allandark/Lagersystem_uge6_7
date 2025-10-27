from flask_restx import Namespace, Resource, fields, Model
from flask_jwt_extended import JWTManager
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash


jwt = JWTManager()

authorizations = {
    "jsonWebToken":{
        "type": "apiKey",
        "in": "header",
        "name": "Authorization"
    }
}




# TEMP: Move to db
test_users = []
test_data = {
    "key1": 1,
    "key2": "value"
}

# TODO: move to config
admin_user: dict[str] = {
            "id": 0,
            "username": "admin",
            "password_hash": generate_password_hash("Password12!")
        }

test_users.append(admin_user)
# END: Test

def create_api_auth(db_manager):

    api: Namespace = Namespace("auth", description="Authentication namespace", authorizations=authorizations)
    # Models
    user_model: Model = api.model('UserModel', {
        'id': fields.Integer(readonly=True, description='Unique user id'),
        'name': fields.String(required=True, description='Name of user')})
    login_model: Model = api.model("LoginModel",{
            "username": fields.String,
            "password": fields.String})
    change_password_model = api.model('ChangePassword', {
        'old_password': fields.String(required=True),
        'new_password': fields.String(required=True),
    })
    change_username_model = api.model('ChangeUsername', {
        'new_username': fields.String(required=True),
    })

    @api.route('/')
    @api.route('/login')
    class Login(Resource):
        ''' Login to user
        '''
        @api.doc('Login to user')
        @api.expect(login_model)    
        def post(self):
            # TEMP: find user from db
            user: dict[str] = None
            
            for u in test_users:
                if u['username'] == api.payload["username"]:            
                    user = u


            status : bool = True
            if not user:
                status = False
            if not check_password_hash(user["password_hash"],api.payload["password"]):
                status = False
            if not status:
                return {"error": "Invalid user or password"}, 401
            return {"access_token": create_access_token(user["username"])}

    @api.route('/register')
    class Register(Resource):
        ''' Register user
        '''

        @jwt_required()  
        @api.doc('Register user',security="jsonWebToken")
        @api.expect(login_model)
        @api.marshal_with(user_model, code=201)
        def post(self):
            user: dict[str] = {
                "id": len(test_users),
                "username": api.payload["username"],
                "password_hash": generate_password_hash(api.payload["password"])
            }

            # TODO: add to db instead
            test_users.append(user)
            
            return {"id": user["id"], "name": user["username"]}, 201


    @api.route('/change_password')
    class ChangePassword(Resource):
        ''' Change password of existing user
        '''
        @jwt_required() 
        @api.doc('Change password',security="jsonWebToken")
        @api.expect(change_password_model)
        # @api.marshal_with( code=200)
        def post(self):
            user_id = get_jwt_identity()
            user: dict[str] = None
            for u in test_users:
                if u['username'] == user_id:
                    user = u
            if not user:
                return {"error": "User does not exist"}, 401

            if not check_password_hash(user["password_hash"],api.payload["old_password"]):
                return {"error": "Wrong old password provided"}, 401
            
            user['password_hash'] = generate_password_hash(api.payload["new_password"])

            return {"message" : "Password updated"}, 200



    @api.route('/change_username')
    class ChangeUsername(Resource):
        ''' Change username of existing user
        '''
        @jwt_required() 
        @api.doc('Change password',security="jsonWebToken")
        @api.expect(change_username_model)
        # @api.marshal_with(code=200)
        def post(self):
            user_id = get_jwt_identity()
            user: dict[str] = None
            for u in test_users:
                if u['username'] == user_id:
                    user = u
            if not user:
                return {"error": "User does not exist"}, 401
            
            # TODO: check valid names
            user['username'] = api.payload['new_username']
            test_users[user['id']] = user
            return {"message" : "Username updated"}, 200



    # TEMP: remove when actual endpoints are there
    @api.route('/tests')
    class Test(Resource):
        ''' Test endpoint
        '''

        @jwt_required()  
        @api.doc('Test endpoint with authentication requirements',security="jsonWebToken")
        def get(self):
            return test_data

    return api

