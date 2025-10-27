from flask_restx import Namespace, Resource, fields, Model
from flask_jwt_extended import jwt_required
from apis.auth import authorizations
from flask import Flask, jsonify, request

api: Namespace = Namespace("orders", description="Order namespace", authorizations=authorizations)

orders_model = api.model('OrderModel', {'id': fields.Integer, 'name': fields.String, 'warelist': fields.String, 'total': fields.Integer})

rmeove_orders_model = api.model('RemoveOrderModel', {'id': fields.Integer})

orders_list = [
    {'id': 0, 'name': "Viktor", 'warelist': ['banana', 'planes', 'car'], 'total': 500},
    {'id': 1, 'name': "Michael", 'warelist': ['sofa', 'bed', 'car'], 'total': 1500},
    {'id': 2, 'name': "Vera", 'warelist': ['glasses', 'flatbed', 'truck'], 'total': 500}
]

@api.route("/<int:id>")
class OrderGet(Resource):
    @api.doc('Get an order based on ID')
    @api.marshal_with(orders_model, skip_none=True, code=200)
    def get(self, id):
        return {"id":id}, 200

@api.route("/")
class Order(Resource):
    
    @api.doc('Receive a new order')
    @api.expect(orders_model)
    def post(self):
        ID = api.payload['id']
        name = api.payload['name']
        warelist = api.payload['warelist']
        total = api.payload['id']
        orders_list.append({'id': {ID}, 'name': {name}, 'warelist': {warelist}, 'total': {total}})
        return jsonify({'New order': list(orders_list[ID])})
    
    @api.doc("Update order")
    @api.expect(orders_model)
    def put(self):
        ID = api.payload['id']
        name = api.payload['name']
        warelist = api.payload['warelist']
        total = api.payload['id']
        orders_list[ID] = f"'id': {ID}, 'name': {name}, 'warelist': {warelist}, 'total': {total}"
        return jsonify({'Updated order': orders_list[ID]})
    
    @api.doc("Delete order")
    @api.expect(rmeove_orders_model)
    def delete(self):
        ID = api.payload['id']
        order = orders_list.pop(ID)
        return jsonify({'Removed order': order}, 200)
    
