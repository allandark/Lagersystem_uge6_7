from flask_restx import Namespace, Resource, fields, Model, reqparse
from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from apis.auth import authorizations

api: Namespace = Namespace("customer", description="Customer namespace", authorizations=authorizations)

customer_dict = dict({1 : "Viktor", 2 : "Dennis", 3: "Luke"})

get_customer_model: Model = api.model('GetCustomerModel', {'id': fields.Integer(required=True, description='Customer ID number')})

@api.route("/customer/<int:id>")
class Customer(Resource):
    
    @api.doc('Get the customer based on the ID number')
    @api.marshal_with(get_customer_model, code = 200)
    def get(self, id):
        customer = customer_dict[id]
        return jsonify({'message': customer})