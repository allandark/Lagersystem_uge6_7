from flask_restx import Namespace, Resource, fields, Model
from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from apis.auth import authorizations


def create_api_product(db_manager):
    api: Namespace = Namespace("product", description="Product namespace", authorizations=authorizations)

    product_list = list(("aluminium", "banana", "apple", "car"))

    new_product_model: Model = api.model('NewProductModel', {
            'id': fields.Integer(required=True, description = "Product ID"),
            'name': fields.String(required=True, description='Name of product'),
            'price': fields.Float(required=True, description="Poduct price")})

    remove_product_model: Model = api.model('RemoveProductModel', {
            'id': fields.Integer(required=True, description='Name of product')})

    update_product_model: Model = api.model('UpdateProductModel', {
            'id': fields.Integer(required=True, description = "Product ID"),
            'name': fields.String(required=True, description='Name of product'),
            'price': fields.Float(required=True, description="Poduct price")})

    @api.route("/<int:id>")
    class ProductGetById(Resource):
        @api.doc('Get product based on ID')
        def get(self, id):
            products = db_manager.products.GetById(id)
            print(products)
            return {"products":products}, 200
        
    @api.route("/<float:price>")
    class ProductGetByPrice(Resource):
        @api.doc('Get product based on price')
        def get(self, price):
            products = db_manager.products.GetByPrice(price)
            print(products)
            return {"products":products}, 200
        
    @api.route("/<float:low_price>/<float:high_price>")
    class ProductGetByPriceInterval(Resource):
        @api.doc('Get product based on price')
        def get(self, low_price, high_price):
            products = db_manager.products.GetPriceByInterval(low_price, high_price)
            print(products)
            return {"products":products}, 200
    
    @api.route("/")
    class Product(Resource):
        @api.doc("Get all products")
        def get(self):
            products = db_manager.products.GetAll()
            return {"products": products}, 200

        @api.doc('Update new product')
        @api.expect(update_product_model)
        def put(self):
            product_ID = api.payload['id']
            result = db_manager.products.GetById(product_ID)
            return jsonify({'New product': result})

        @api.doc('Remove product')
        @api.expect(remove_product_model)
        def delete(self):
            ID = api.payload['id']
            result = db_manager.products.GetById(ID)
            return jsonify({'Removed product': result})


        @api.doc('New product')
        @api.expect(new_product_model)
        def post(self):
            product_id = api.payload['id']
            product_name = api.payload['name']
            product_price = api.payload['price']
            #if(len(db_manager.products.GetById(product_id)) > 0):
             #   return jsonify({"message": f"Product {product_id} already exists!"})
            #else:
            result = db_manager.products.insertproduct(product_name, product_price)
            return jsonify({'Added product': result})
    
    return api