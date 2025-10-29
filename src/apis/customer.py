from flask_restx import Namespace, Resource, fields, Model, reqparse
from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from apis.auth import authorizations


def create_api_customer(db_manager):
    api: Namespace = Namespace("customer", description="Customer namespace", authorizations=authorizations)

    customer_dict = [
    {"id":0, "name": "Dennis"},
    {"id":1, "name": "Viktor"},
    {"id":2, "name": "Luke"},
    ]

    new_customer_model: Model = api.model('NewCustomerModel', {'customerid': fields.Integer(required=True, description='Customer ID number'),
                                            'name': fields.String(required=True, description='Name of customer'),
                                            'email': fields.String(required=True, description="Customer email")})

    update_customer_model: Model = api.model('NewCustomerModel', {'customerid': fields.Integer(required=True, description='Customer ID number'),
                                            'name': fields.String(required=True, description='Name of customer'),
                                            'email': fields.String(required=True, description="Customer email")})

    remove_customer_model: Model = api.model('RemoveCustomerModel', {'id': fields.Integer(required=True, description='Customer ID number')})
    
    @api.route("/<int:id>")
    class CustomerGet(Resource):
        
        @api.doc('Get the customer based on the ID number')
        def get(self, id):
            result = db_manager.customers.GetById(id)
            return result
        
    @api.route("/")
    class Customer(Resource):

        @api.doc('Get all customers')
        def get(self):
            result = db_manager.customers.GetAll()
            return result

        @api.doc('Add a new customer')
        @api.expect(new_customer_model)
        def post(self):
            ID = api.payload['customerid']
            name = api.payload['name']
            email = api.payload['email']
            if ((ID == 0) or (name == "") or (email == "")):
                return jsonify({"message": "Invalid customer"}, 404)
            else:
                result = db_manager.customers.Insert(name, email)
                return result

        @api.doc('Update customer info')
        @api.expect(update_customer_model)
        def put(self):
            ID = api.payload['customerid']
            name = api.payload['name']
            email = api.payload['email']
            result = db_manager.customers.GetById(ID)
            if ID == 0:
                return jsonify({"message": "Invalid customer"}, 404)
            else:
                result = db_manager.customers.Update(ID, name, email)
                return result
            
        @api.doc('Delete a customer')
        @api.expect(remove_customer_model)
        def delete(self):
            ID = api.payload['id']
            if ID == 0:
                return jsonify({"message": "Invalid customer"}, 404)
            else:
                result = db_manager.customers.Delete(ID)
            return result

    return api