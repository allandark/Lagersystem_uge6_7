from flask_restx import Namespace, Resource, fields, Model
from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from flask_jwt_extended import jwt_required
from apis.auth import authorizations

def create_api_product(db_manager):
    api: Namespace = Namespace("product", description="Product namespace", authorizations=authorizations)

    #product_list = list(("aluminium", "banana", "apple", "car"))

    new_product_model: Model = api.model('NewProductModel', {
            'id': fields.Integer(required=True, description = "Product ID"),
            'name': fields.String(required=True, description='Name of product'),
            'price': fields.Float(required=True, description="Poduct price"),
            'status': fields.String})

    remove_product_model: Model = api.model('RemoveProductModel', {
            'id': fields.Integer(required=True, description='Name of product')})

    update_product_model: Model = api.model('UpdateProductModel', {
            'id': fields.Integer(required=True, description = "Product ID"),
            'name': fields.String(required=True, description='Name of product'),
            'price': fields.Float(required=True, description="Poduct price"),
            'status': fields.String})

    @api.route("/<int:id>")
    class ProductGetById(Resource):
        @api.doc('Get product based on ID')
        def get(self, id):
            products = db_manager.product.GetById(id)
            # print(products)
            return products, 200


        @jwt_required()
        @api.doc('Update new product', security='jsonWebToken')
        @api.expect(update_product_model)
        def put(self, id):
            product_ID = id
            product_name = api.payload['name']
            product_price = api.payload['price']
            product_status = api.payload['status']
            result = db_manager.product.GetById(product_ID)
            if result is False:
                return {"error": "not found"}, 404
            result = db_manager.product.UpdateProduct(
                product_ID, 
                product_name, 
                product_price,
                product_status)
            return  result, 201

        @jwt_required()
        @api.doc('Remove product', security='jsonWebToken')
        @api.expect(remove_product_model)
        def delete(self, id):
            ID = api.payload['id']
            result = db_manager.product.GetById(ID)
            if result == []:
                return jsonify({"message": "Product doesn't exist"})
            else:
                db_manager.product.UpdateItemStatus(ID, "Inactive")
            #result = db_manager.product.RemoveItem(ID)
            return jsonify({'Removed product': result})
        
    @api.route("price/<float:price>")
    class ProductGetByPrice(Resource):
        @api.doc('Get product based on price')
        def get(self, price):
            newPrice = float (price)
            products = db_manager.product.GetByPrice(price)
            print(products)
            return {"products":products}, 200
        
    @api.route("/price-range/<float:range>")
    class ProductGetByPriceInterval(Resource):
        @api.doc('Get product based on price')
        def get(self, range):
            low_price, high_price = map(float, range.split('-'))
            products = db_manager.product.GetPriceByInterval(low_price, high_price)
            print(products)
            return {"products":products}, 200
            
    @api.route("/")
    class Product(Resource):
        @api.doc("Get all products")
        def get(self):
            products = db_manager.product.GetAll()
            return products, 200


        @jwt_required()
        @api.doc('New product', security='jsonWebToken')
        @api.expect(new_product_model)
        def post(self):
            product_id = api.payload['id']
            product_name = api.payload['name']
            product_price = api.payload['price']
            result = db_manager.product.insertproduct(product_name, product_price)
            return result, 201
    
    return api