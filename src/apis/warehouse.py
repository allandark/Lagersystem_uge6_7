from flask_restx import Namespace, Resource, fields, Model
from apis.auth import authorizations

api: Namespace = Namespace("warehouse", description="Warehouse namespace", authorizations=authorizations)


warehouse_model = api.model("WarehouseModel",{
    "id": fields.Integer,
    "name": fields.String
})

#TEMP: test
warehouses = [
    {"id": 0, "name":"Odense"},
    {"id": 1, "name":"Middelfart"},
]


@api.route('/')
class WarehouseList(Resource):

    @api.doc( description='Get list of warehouses')
    @api.marshal_list_with(warehouse_model, code=200)
    def get(self,):        

        return warehouses, 200

@api.route('/<int:wh_id>')
class WarehouseDetail(Resource):
    
    @api.doc(params={'lager_id': 'ID of the lager'}, description='Get warehouse by ID')
    @api.marshal_with(warehouse_model, code=200)
    def get(self, wh_id):
        result = any(w['id'] == wh_id for w in warehouses)
        if not result:
            return {"error": "bad argument"}, 400
        return warehouses[wh_id], 200


    # def put(self):
    #     pass

    # def post(self):
    #     pass

    # def delete(self):
    #     pass
