| Method | Endpoint               | Description              | Auth Required | Payload Model     | Response Code |
|--------|------------------------|--------------------------|---------------|-------------------|----------------|
| GET    | `/warehouses`           | Get all warehouses       | No     | None              | 200            |
| GET    | `/warehouses/<id>`       | Get a specific warehouse | No    | None              | 200 / 404      |
| POST   | `/warehouses`            | Create a new warehouse   | Yes (JWT)     | warehouse_model   | 201 / 400      |
| PUT    | `/warehouses/<id>`       | Update a warehouse       | Yes (JWT)     | warehouse_model   | 200 / 404      |
| DELETE | `/warehouses/<id>`       | Delete a warehouse       | Yes (JWT)     | None              | 200 / 404      |


| Method | Endpoint                                      | Description                          | Auth Required | Payload Model         | Response Code |
|--------|-----------------------------------------------|--------------------------------------|---------------|------------------------|----------------|
| GET    | `/warehouses/<id>/inventory`                    | Get all inventory items              | No     | None                   | 200 / 404      |
| GET    | `/warehouses/<id>/inventory/<item_id>`          | Get a specific inventory item        | No     | None                   | 200 / 404      |
| POST   | `/warehouses/<id>/inventory`                    | Add a new inventory item             | Yes (JWT)     | inventory_model        | 201 / 400      |
| PUT    | `/warehouses/<id>/inventory/<item_id>`          | Update an inventory item             | Yes (JWT)     | inventory_model        | 200 / 404      |
| DELETE | `/warehouses/<id>/inventory/<item_id>`          | Delete an inventory item             | Yes (JWT)     | None                   | 204 / 404      |