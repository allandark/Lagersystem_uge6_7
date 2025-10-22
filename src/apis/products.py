from flask_restx import Namespace, Resource, fields, Model
from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from apis.auth import authorizations

api: Namespace = Namespace("product", description="Product namespace", authorizations=authorizations)

product_list = list(("aluminium", "banana", "apple", "car"))

get_product_model: Model = api.model('ProductModel', {
        'ID': fields.Integer(required=True, description='ID of product')})

@api.route("/product")
class Product(Resource):
    @api.doc('Get product based on ID')
    @api.expect(get_product_model)
    def get(self):
        ID = api.payload('ID')
        result = product_list[ID]
        return jsonify({'product': result})
    
    def put(self, product):
        product_list.append(product)
        return jsonify({'New product': product_list})

    def delete(self, ID):
        result = product_list.pop(ID)
        return jsonify({'Removed product': result})

    def post(self, ID, new_product):
        product_list[ID] = new_product
        return jsonify({'Updated product': product_list[ID]})
