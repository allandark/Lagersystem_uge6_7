import mysql.connector

class ProductModel:
    def __init__(self, db):
        self.db = db 
    
    def GetAll(self):

        self.db.execute("SELECT * FROM produkts")

        myresult = self.db.fetchall()
        
        return myresult

    def GetbyId(self, id):

        self.db.execute(f"SELECT * FROM produkts where produktID = %s ", (id,))

        myresult = self.db.fetchall()
        
        return myresult


    def GetbyPrise(self, pris):

        self.db.execute(f"SELECT * FROM produkts where pris = %s ", (pris,))

        myresult = self.db.fetchall()
        
        return myresult

    def GetPricebyiterval(self, lov_price,high_price):

        self.db.execute(f"SELECT * FROM produkts WHERE pris BETWEEN %s AND %s" , (lov_price,high_price))

        myresult = self.db.fetchall()
        
        return myresult

    def insertproduct(self, name, price):

        query = "INSERT INTO produkts (navn, pris) VALUES (%s, %s)"

        self.db.execute(query, (name, price))
        self.db.commit()

    def GetbyName(self, name):

        self.db.execute(f"SELECT * FROM produkts where navn = %s ", (name,))

        myresult = self.db.fetchall()
        
        return myresult

    def exist(self,id):

        self.db.execute(f"SELECT exists(select 1 from produkts where produktID = %s)AS id_exists ", (id,))

        myresult = self.db.fetchall()

        if myresult == [(0,)]:
            return False
        else:
            return True

