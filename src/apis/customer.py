from flask_restx import Namespace, Resource, fields, Model
from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from apis.auth import authorizations

api: Namespace = Namespace("customer", description="Customer namespace", authorizations=authorizations)



class Customer(Resource):
    
    def get(self):
        return jsonify({'message': 'customer'})