from flask_restx import Namespace, Resource, fields, Model
from flask_jwt_extended import jwt_required
from apis.auth import authorizations


api: Namespace = Namespace("warehouse", description="Warehouse namespace", authorizations=authorizations)


warehouse_model = api.model("WarehouseModel",{
    "id": fields.Integer,
    "name": fields.String
})

warehouse_item_model = api.model("WarehouseItemModel",{
    "id": fields.Integer,
    "product_id": fields.Integer,
    "warehouse_id": fields.Integer,
    "quantity": fields.Integer
})

#TEMP: test

items=[
    {"id": 0, "unit_price": 500, "name": "laptop"},
    {"id": 1, "unit_price": 50, "name": "pc mouse"},
    {"id": 2, "unit_price": 150, "name": "pc keyboard"},
]

warehouses = [
    {"id": 0, "name":"Odense"},
    {"id": 1, "name":"Middelfart"},
]

warehouse_items = [
    {"id": 0, "product_id":0, "warehouse_id": 0, "quantity": 5},
    {"id": 1, "product_id":1, "warehouse_id": 0, "quantity": 10},
    {"id": 2, "product_id":2, "warehouse_id": 0, "quantity": 15},
    {"id": 3, "product_id":0, "warehouse_id": 1, "quantity": 15},
    {"id": 4, "product_id":1, "warehouse_id": 1, "quantity": 5},
    {"id": 5, "product_id":2, "warehouse_id": 1, "quantity": 20}
]
# END TEMP

@api.route('/')
class WarehouseList(Resource):

    @api.doc( description='Get list of warehouses')
    @api.marshal_list_with(warehouse_model, code=200)
    def get(self,):        
        return warehouses, 200

    @jwt_required()
    @api.doc(
        description="Create new warehouse",
        security="jsonWebToken"
        )
    @api.expect(warehouse_model)
    @api.marshal_with(warehouse_model, code=200)
    def post(self):
        wh = {
            "id": len(warehouses),
            "name": api.payload['name']
        }
        warehouses.append(wh)
        return wh, 201

@api.route('/<int:id>')
class WarehouseDetail(Resource):
    
    @api.doc(
        description='Get warehouse by ID')
    @api.marshal_with(warehouse_model, code=200)
    def get(self, id):
        wh = next((w for w in warehouses if w['id'] == id), None)
        if not wh:
            return {"error": "warehouse not found"}, 404
        return wh, 200

    @jwt_required()
    @api.doc(
        description='Update warehouse of ID',
        security="jsonWebToken")
    @api.expect(warehouse_model)
    @api.marshal_with(warehouse_model, code=200)
    def put(self, id):
        # find warehouse
        wh = next((w for w in warehouses if w['id'] == id), None)
        if not wh:
            return {"error": "warehouse does not exist"}, 400
        # update warehouse
        wh['id'] = api.payload['id']
        wh['name'] = api.payload['name']
        return wh, 200

        
    @jwt_required()
    @api.doc( 
        description='Delete warehouse of ID',
        security="jsonWebToken")
    def delete(self, id):
        wh = next((w for w in warehouses if w['id'] == id), None)
        if not wh:
            return {"error": "warehouse not found"}, 404

        for i, w in enumerate(warehouses):
            if w['id'] == id:
                del warehouses[i]
                break

        return {"message": "warehouse deleted"}, 200


@api.route('/<int:id>/inventory')
class InventoryDetail(Resource):
    
    @api.doc( 
        description='Get inventory of warehouse with ID')
    @api.marshal_list_with(warehouse_item_model)
    def get(self,id):
        wh = next((w for w in warehouses if w['id'] == id), None)
        if not wh:
            return {"error": "warehouse not found"}, 404

        inventory = [i for i in warehouse_items if i['warehouse_id'] == id]
        return inventory, 200
        
    
    @jwt_required()
    @api.doc( 
        description='Create inventory item of warehouse with ID',
        security="jsonWebToken")
    @api.expect(warehouse_item_model)
    @api.marshal_with(warehouse_item_model)
    def post(self,id):
        wh = next((w for w in warehouses if w['id'] == id), None)
        if not wh:
            return {"error": "warehouse not found"}, 404

        item = {
            "id": len(warehouse_items),
            "product_id": api.payload['product_id'],
            "warehouse_id": api.payload['warehouse_id'],
            "quantity": api.payload['quantity']
        }
        warehouse_items.append(item)
        return item, 201

@api.route('/<int:id>/inventory/<int:item_id>')
class InventoryList(Resource):
    
    @api.doc( 
        description='Get inventory item with item_id from warehouse with ID')
    @api.marshal_with(warehouse_item_model)
    def get(self,id,item_id):
        wh = next((w for w in warehouses if w['id'] == id), None)
        if not wh:
            return {"error": "warehouse not found"}, 404
        item = next((i for i in warehouse_items if i['id'] == item_id), None)
        if not item:
            return {"error": "item not found"}, 404
        return item, 200

    @jwt_required()
    @api.doc( 
        description='Update inventory item with item_id from warehouse with ID',
        security="jsonWebToken")
    @api.expect(warehouse_item_model)
    @api.marshal_with(warehouse_item_model)
    def put(self,id,item_id):
        wh = next((w for w in warehouses if w['id'] == id), None)
        if not wh:
            return {"error": "warehouse not found"}, 404
        item = next((i for i in warehouse_items if i['id'] == item_id), None)
        if not item:
            return {"error": "item not found"}, 404
        
        item['product_id'] = api.payload['product_id']
        item['warehouse_id'] = api.payload['warehouse_id']
        item['quantity'] = api.payload['quantity']
        return item, 200

    @jwt_required()
    @api.doc( 
        description='Delete inventory item with item_id from warehouse with ID',
        security="jsonWebToken")
    def delete(self,id,item_id):
        wh = next((w for w in warehouses if w['id'] == id), None)
        if not wh:
            return {"error": "warehouse not found"}, 404
        item = next((i for i in warehouse_items if i['id'] == item_id), None)
        if not item:
            return {"error": "item not found"}, 404

        for i, w in enumerate(warehouse_items):
            if w['id'] == item_id:
                del warehouse_items[i]
                break
            
        return {"message": "inventory deleted"}, 200