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
            users = db_manager.admin.GetAll()
            user = next((u for u in users if u["name"] == api.payload["username"]), None)

            status : bool = True
            if user is None:
                status = False
            elif not check_password_hash(user["password_hash"],api.payload["password"]):
                status = False

            if not status:
                return {"error": "Invalid user or password"}, 401

            return {"access_token": create_access_token(identity=str(user["id"]))}

    @api.route('/register')
    class Register(Resource):
        ''' Register user
        '''

        @jwt_required()  
        @api.doc('Register user',security="jsonWebToken")
        @api.expect(login_model)
        @api.marshal_with(user_model, code=201)
        def post(self):

            user = db_manager.admin.Insert( 
                api.payload["username"],
                generate_password_hash(api.payload["password"]))

            return user, 201


    @api.route('/change_password')
    class ChangePassword(Resource):
        ''' Change password of existing user
        '''
        @jwt_required() 
        @api.doc('Change password',security="jsonWebToken")
        @api.expect(change_password_model)
        # @api.marshal_with( code=200)
        def post(self):
            user_id = int(get_jwt_identity())
            user = db_manager.admin.GetById(user_id)
        
            if user is False:
                return {"error": "User does not exist"}, 404

            if not check_password_hash(user["password_hash"],api.payload["old_password"]):
                return {"error": "Wrong old password provided"}, 401
            
            user = db_manager.admin.Update(
                admin_id=user["id"],
                name=user["name"],
                password_hash=generate_password_hash(api.payload["new_password"])
            )
            if user is False:
                return {"error": "could not change password"}, 401

            return user, 200



    @api.route('/change_username')
    class ChangeUsername(Resource):
        ''' Change username of existing user
        '''
        @jwt_required() 
        @api.doc('Change password',security="jsonWebToken")
        @api.expect(change_username_model)
        # @api.marshal_with(code=200)
        def post(self):
            user_id = int(get_jwt_identity())
            user = db_manager.admin.GetById(user_id)

            if user is False:
                return {"error": "User does not exist"}, 404
            
           
            user = db_manager.admin.Update(
                admin_id=user["id"],
                name=api.payload["new_username"],
                password_hash=user["password_hash"])
            
            return user, 200

    @api.route('/profile/me')
    class ProfileMe(Resource):
        ''' Profile me
        '''
        @jwt_required() 
        @api.doc('Returns the current user from JWT',security="jsonWebToken")
        @api.marshal_with(user_model, code=200)
        def get(self):
            user_id = int(get_jwt_identity())
            user = db_manager.admin.GetById(user_id)
            if user is False:
                return {"error": "user not found"}, 404
            return {"id": user["id"], "name": user["name"]}, 200

    @api.route('/profile/')
    class ProfileAll(Resource):
        ''' Get all admin users
        '''
        @jwt_required() 
        @api.doc('Returns all the admin users',security="jsonWebToken")
        @api.marshal_list_with(user_model, code=200)
        def get(self):
            users = db_manager.admin.GetAll()
            return users, 200

    @api.route('/profile/<int:id>')
    class ProfileID(Resource):
        ''' Get admin user by id
        '''
        @jwt_required() 
        @api.doc('Returns the admin user by id',security="jsonWebToken")
        @api.marshal_with(user_model, code=200)
        def get(self, id):
            user = db_manager.admin.GetById(id)
            if user is False:
                return {"error": "user not found"}, 404
            return user, 200

    return api

