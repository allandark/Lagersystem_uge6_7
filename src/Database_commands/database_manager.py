import mysql.connector
from database_commands.product import ProductModel
from database_commands.orders import OrdersModel
from database_commands.admin import AdminModel
from database_commands.customers import CustomersModel
from database_commands.warehouse_inventory import WarehuseInventoryModel
from database_commands.warehouse import WarehouseModel

class DatabaseManager:
    def __init__(self, host, user, password, dbname):
        
        try:
            self.mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=dbname
            )
            
        
            self.product = ProductModel(self.mydb)
            self.orders = OrdersModel(self.mydb)
            self.admin = AdminModel(self.mydb)
            self.customers = CustomersModel(self.mydb)
            self.warehouse = WarehouseModel(self.mydb)
            self.warehouse_inventory = WarehuseInventoryModel(self.mydb)
        
        finally:
            if 'connection' in locals() and self.mydb.is_connected():
                self.mydb.close()
        
    def is_connected(self):
        
        if self.mydb.is_connected():
            return True
        else:
            return False

        
    
    