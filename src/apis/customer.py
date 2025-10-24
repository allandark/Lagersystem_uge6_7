from flask_restx import Namespace, Resource, fields, Model, reqparse
from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from apis.auth import authorizations

api: Namespace = Namespace("customer", description="Customer namespace", authorizations=authorizations)

customer_dict = [
{"id":0, "name": "Dennis"},
{"id":1, "name": "Viktor"},
{"id":2, "name": "Luke"},
]
get_customer_model: Model = api.model('GetCustomerModel', {'id': fields.Integer(required=True, description='Customer ID number'),
                                        'name': fields.String(required=True, description='Name of customer')})

new_customer_model: Model = api.model('NewCustomerModel', {'id': fields.Integer(required=True, description='Customer ID number'),
                                        'name': fields.String(required=True, description='Name of customer')})

update_customer_model: Model = api.model('UpdateCustomerModel', {'id': fields.Integer(required=True, description='Customer ID number'),
                                        'new_name': fields.String(required=True, description='New name of customer')})

remove_customer_model: Model = api.model('RemoveCustomerModel', {'id': fields.Integer(required=True, description='Customer ID number'),
                                        'name': fields.String(required=True, description='New name of customer')})
@api.route("/<int:id>&<string:name>")
class CustomerGet(Resource):
    
    @api.doc('Get the customer based on the ID number')
    @api.marshal_with(get_customer_model, code = 200)
    def get(self, id, name):
        customer = customer_dict[id]
        return jsonify({"Customer": id}), 200
    
@api.route("/new")
class CustomerPost(Resource):
    @api.doc('Add a new customer')
    @api.expect(new_customer_model)
    def post(self):
        ID = api.payload['id']
        name = api.payload['name']
        customer_dict.append({"id": ID, "name": name}) 
        return jsonify({'New customer': customer_dict[ID]})
    
@api.route("/update")
class CustomerUpdate(Resource):

    @api.doc('Update customer info')
    @api.expect(update_customer_model)
    def put(self):
        ID = api.payload['id']
        name = api.payload['new_name']
        customer_dict[ID] = {"id": ID, "name": name}
        return jsonify({"Updated customer": customer_dict[ID]})
    
@api.route("/remove")
class CustomerDelete(Resource):

    api.doc('Delete a customer')
    api.expect(remove_customer_model)
    def delete(self):
        ID = api.payload['id']
        customer_dict.pop(ID)
        return jsonify({'Removed customer': customer_dict})