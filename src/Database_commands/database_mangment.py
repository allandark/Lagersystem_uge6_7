from mysql import connector
from product import ProductModel

class Database_mangment:
    def __init__(self, host, user, password, dbName):
        
        try:
            self.mydb = connector.connect(
                host=host,
                user=user,
                password=password,
                database=dbName
            )
        
            self.product = ProductModel(self.mydb.cursor())
        
        finally:
            if 'connection' in locals() and self.mydb.is_connected():
                self.mydb.close()
        
    def isconnect(self):
        if self.mydb.is_connected():
            return True
        else:
            return False

        
    
    