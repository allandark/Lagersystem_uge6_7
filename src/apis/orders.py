from flask_restx import Namespace, Resource, fields, Model
from flask_jwt_extended import jwt_required
from apis.auth import authorizations
from flask import Flask, jsonify, request

api: Namespace = Namespace("Orders", description="Order namespace", authorizations=authorizations)

orders_model = api.model('OrderModel', {'id': fields.Integer, 'name': fields.String, 'warelist': fields.List, 'total': fields.Integer})

orders = [
    {'id': 0, 'name': "Viktor", 'warelist': ['banana', 'planes', 'car'], 'total': 500},
    {'id': 1, 'name': "Michael", 'warelist': ['sofa', 'bed', 'car'], 'total': 1500},
    {'id': 2, 'name': "Vera", 'warelist': ['glasses', 'flatbed', 'truck'], 'total': 500}
]

class Order(Resource):

    @api.doc('Get an order based on ID')
    def get(self):
        return jsonify({'message': 'This is a test'}), 200
    
    @api.doc('Receive a new order')
    @api.expect(orders_model)
    def post(self):
        ID = api.payload['id']
        name = api.payload['name']
        warelist = api.payload['warelist']
        total = api.payload['id']
        orders.append({'id': {ID}, 'name': {name}, 'warelist': {warelist}, 'total': {total}})
        return jsonify({'New order': orders[ID]}), 200
    
