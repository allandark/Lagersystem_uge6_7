import mysql.connector

class adminmodel:
    
    def __init__(self, db):
        self.db = db
        
    def adminGetAll(self):
        
        try:
            self.db.execute("SELECT * FROM admin")

            myresult = self.db.fetchall()
            
            return myresult
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False


    def adminGetbyId(self, id):
        
        try:
            self.db.execute(f"SELECT * FROM admin where adminid = %s ", (id,))

            myresult = self.db.fetchall()
            
            return myresult
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False
        
    def admininsert(self, name,password):
        
        try:
            query = "INSERT INTO admin (navn, adminpassword) VALUES (%s, %s)"

            self.db.execute(query, (name, password))
            self.db.commit()
            return True
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False
        
    def adminupdateName(self, adminid,newName):
        
        try:
            query = "UPDATE admin SET navn = %s WHERE adminid = %s"

            self.db.execute(query, (newName, adminid))
            self.db.commit()
            return True
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False
        
    def adminupdatePassword(self,adminid,adminpassword):
        
        try:
            query = "UPDATE admin SET adminpassword = %s WHERE adminid = %s"

            self.db.execute(query, (adminpassword, adminid))
            self.db.commit()
            return True
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False