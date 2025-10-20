from flask_restx import fields, Api, Resource

def get_user_model(api):
    return api.model('User', {
        'id': fields.Integer(readonly=True, description='Unique user id'),
        'name': fields.String(required=True, description='Name of user'),        
    })

def get_login_model(api):
    return api.model("LoginModel",{
        "username": fields.String,
        "password": fields.String
    })


