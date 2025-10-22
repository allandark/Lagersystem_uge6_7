from flask_restx import Namespace, Resource, fields, Model
from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from apis.auth import authorizations

api: Namespace = Namespace("product", description="Product namespace", authorizations=authorizations)

product_list = list(("aluminium", "banana", "apple", "car"))

@api.route("/product")
class Product(Resource):
    @api.doc('Get product based on ID')
    def get(self):
        result = product_list[1]
        return jsonify({'product': result})
    
    #def put(self):
     #   db.create()

    #def delete(self):
     #   db.delete()

    #def post(self):
     #   db.update()
