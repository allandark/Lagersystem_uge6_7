import mysql.connector

class AdminModel:
    
    def __init__(self, db):
        self.db = db
        
    def GetAll(self):
        
        try:
            with self.db.cursor() as cursor:
                cursor.execute("SELECT * FROM admin")
                myresult = cursor.fetchall() 
                return myresult
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False


    def GetById(self, id):
        
        try:
            with self.db.cursor() as cursor:
                cursor.execute(f"SELECT * FROM admin where adminid = %s ", (id,))
                myresult = cursor.fetchall()
                return myresult
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False
        
    def Insert(self, name,password):
        
        try:
            with self.db.cursor() as cursor:
                query = "INSERT INTO admin (navn, adminpassword) VALUES (%s, %s)"
                cursor.execute(query, (name, password))
            self.db.commit()
            return True
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False
        
    def UpdateName(self, adminid,newName):
        
        try:
            with self.db.cursor() as cursor:
                query = "UPDATE admin SET navn = %s WHERE adminid = %s"
                cursor.execute(query, (newName, adminid))
            self.db.commit()
            return True
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False
        
    def UpdatePassword(self,adminid,adminpassword):
        
        try:
            with self.db.cursor() as cursor:
                query = "UPDATE admin SET adminpassword = %s WHERE adminid = %s"
                cursor.execute(query, (adminpassword, adminid))
            self.db.commit()
            return True
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False