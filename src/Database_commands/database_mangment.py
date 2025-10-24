from mysql import connector
from product import ProductModel

class Database_mangment:
    def __init__(self, host, user, password, dbName):
        
        
        self.mydb = connector.connect(
            host=host,
            user=user,
            password=password,
            database=dbName
        )
        
        self.product = ProductModel(self.mydb.cursor())
        
        
        
    def isconnect():
        return True
        
    
    