import mysql.connector

class ProductModel:
    
    def __init__(self, db):
        self.db = db 
    
    def GetAll(self):
        
        try:
            
            self.db.execute("SELECT * FROM produkts")

            myresult = self.db.fetchall()
        
            return self._totuple(myresult)
        except Exception as e:
            print("Error getting product:", e)
            return False

    def GetById(self, id):
        
        try:
            self.db.execute(f"SELECT * FROM produkts where produktID = %s ", (id,))

            myresult = self.db.fetchall()
            result = {
                "id": myresult[0][0],
                "price": myresult[0][1],
                "name": myresult[0][2]
            }
            return result
        
        except Exception as e:
            print("Error getting product by id:", e)
            return False

    def GetByPrice(self, price):
        
        try:
            self.db.execute(f"SELECT * FROM produkts where pris = %s ", (price,))

            myresult = self.db.fetchall()
        
            return self._totuple(myresult)
        except Exception as e:
            print("Error getting product by price:", e)
            return False

    def GetPriceByiterval(self, lov_price,high_price):
        
        try:
            self.db.execute(f"SELECT * FROM produkts WHERE pris BETWEEN %s AND %s" , (lov_price,high_price))

            myresult = self.db.fetchall()
        
            return self._totuple(myresult)
        except Exception as e:
            print("Error getting product in price interval:", e)
            return False
            
    def insertproduct(self, name, price):
        
        try:
            query = "INSERT INTO produkts (navn, pris) VALUES (%s, %s)"

            self.db.execute(query, (name, price))
            self.db.commit()
            return True
        except Exception as e:
            print("Error inserting product:", e)
            return False

    def GetbyName(self, name):
        
        try:
            self.db.execute(f"SELECT * FROM produkts where navn = %s ", (name,))

            myresult = self.db.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting product by name:", e)
            return False
        
    def exist(self,id):
        try:
            self.db.execute(f"SELECT exists(select 1 from produkts where produktID = %s)AS id_exists ", (id,))

            myresult = self.db.fetchall()

            if myresult == [(0,)]:
                return False
            else:
                return True
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False
        
    def _totuple(self, myresult):
        result = {
                "id": myresult[0][0],
                "price": myresult[0][1],
                "name": myresult[0][2]
            }
        return result
