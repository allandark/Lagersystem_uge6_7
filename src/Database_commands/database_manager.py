import mysql.connector
from database_commands.product import ProductModel
from database_commands.orders import Ordersmodel
from database_commands.admin import adminmodel
from database_commands.customers import customersModel
from database_commands.lager_manger import lager_mangerModel
from database_commands.lagers import lagermodel

class DatabaseManager:
    def __init__(self, host, user, password, dbname):
        
        try:
            self.mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=dbname
            )
            
        
            self.products = ProductModel(self.mydb.cursor())
            self.orders = Ordersmodel(self.mydb.cursor())
            self.admin = adminmodel(self.mydb.cursor())
            self.customers = customersModel(self.mydb.cursor())
            self.lagers = lagermodel(self.mydb.cursor())
            self.lager_manger = lager_mangerModel(self.mydb.cursor())
        
        finally:
            if 'connection' in locals() and self.mydb.is_connected():
                self.mydb.close()
        
    def isconnect(self):
        
        if self.mydb.is_connected():
            return True
        else:
            return False

        
    
    