import mysql.connector

class ProductModel:
    
    def __init__(self, db):
        self.db = db 
    
    def GetAll(self):
        
        try:
            with self.db.cursor() as cursor:
                cursor.execute("SELECT * FROM produkts")

                myresult = cursor.fetchall()
        
                return myresult
        except Exception as e:
            print("Error getting product:", e)
            return False

    def GetById(self, id):
        
        try:
            with self.db.cursor() as cursor:
                cursor.execute(f"SELECT * FROM produkts where produktID = %s ", (id,))
                if(cursor.with_rows==True):
                    myresult = (cursor.fetchall())
                    return myresult
                else:
                    myresult = cursor.fetchwarnings()
                    return False
                
        except Exception as e:
            print("Error getting product by id:", e)
            return False

    def GetByPrice(self, price):
        
        try:
            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute(f"SELECT * FROM produkts where pris = %s ", (price,))

                myresult = cursor.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting product by price:", e)
            return False

    def GetPriceByInterval(self, lov_price,high_price):
        
        try:
            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute(f"SELECT * FROM produkts WHERE pris BETWEEN %s AND %s" , (lov_price,high_price))

                myresult = cursor.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting product in price interval:", e)
            return False
            
    def insertproduct(self, name, price):
        
        try:
            n_id = -1
            with self.db.cursor(dictionary=True) as cursor:
                query = f"INSERT INTO produkts (navn, pris) VALUES ('{name}', {price})"

                cursor.execute(query)
                n_id = cursor.lastrowid
                # if(cursor.with_rows==True):
                #     result = cursor.fetchall()
                #     return self._totuple(result)
                # else:
                #     result = cursor.fetchwarnings()
                #     return result
            self.db.commit()
            product = {
                "id": n_id,
                "name":  name,
                "price": price
            }
            return product
        except Exception as e:
            print("Error inserting product:", e)
            return False

    def GetbyName(self, name):
        
        try:
            with self.db.cursor(dictionary=True) as cursor:
                cursor.execute(f"SELECT * FROM produkts where navn = %s ", (name,))

                myresult = cursor.fetchall()
        
            return self._totuple(myresult)
        except Exception as e:
            print("Error getting product by name:", e)
            return False
        
    def exist(self,id):
        try:
            with self.db.cursor(dictionary = True) as cursor:
                cursor.execute(f"SELECT exists(select 1 from produkts where produktID = %s)AS id_exists ", (id,))

                myresult = cursor.fetchall()

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
