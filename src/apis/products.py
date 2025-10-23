from flask_restx import Namespace, Resource, fields, Model
from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from apis.auth import authorizations

api: Namespace = Namespace("product", description="Product namespace", authorizations=authorizations)

product_list = list(("aluminium", "banana", "apple", "car"))

get_product_model: Model = api.model('GetProductModel', {'id': fields.Integer(required=True, description='ID of product')})

new_product_model: Model = api.model('NewProductModel', {
        'name': fields.String(required=True, description='Name of product')})

remove_product_model: Model = api.model('RemoveProductModel', {
        'id': fields.Integer(required=True, description='Name of product')})

update_product_model: Model = api.model('UpdateProductModel', {
        'id': fields.Integer(required=True, description='Name of product'),
        'status': fields.String(required=True, description='New status of product')})

@api.route("/product")
class Product(Resource):
    @api.doc('Get product based on ID')
    @api.expect(get_product_model)
    def get(self):
        id = api.payload['id']
        return jsonify({'product': product_list[id]})
    
    @api.doc('Add new product')
    @api.expect(new_product_model)
    def put(self):
        product = api.payload['name']
        product_list.append(product)
        return jsonify({'New product': product_list})

    @api.doc('Remove product')
    @api.expect(remove_product_model)
    def delete(self):
        ID = api.payload['id']
        result = product_list.pop(ID)
        return jsonify({'Removed product': result})


    @api.doc('Update product')
    @api.expect(update_product_model)
    def post(self):
        ID = api.payload['id']
        status = api.payload['status']
        product_list[ID] = status
        return jsonify({'Updated product': product_list[ID]})
