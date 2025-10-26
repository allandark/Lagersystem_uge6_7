import mysql.connector


class customersModel:

    def __init__(self, db):
        self.db = db
        
    def customersGetAll(self):
        
        try:
            self.db.execute("SELECT * FROM customers")

            myresult = self.db.fetchall()
            
            return myresult
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False


    def customersbyId(self, id):

        try:
            self.db.execute(f"SELECT * FROM customers where customerid = %s ", (id,))

            myresult = self.db.fetchall()
            
            return myresult
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False
        
    def customersinsert(self,name,Email):

        try:
            query = "INSERT INTO customers (navn, Email) VALUES (%s, %s)"

            self.db.execute(query, (name, Email))
            self.db.commit()
            
            return True
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False
        
    def customerUpdateName(self, customerid,newName):

        try:
            query = "UPDATE customers SET navn = %s WHERE customerid = %s"

            self.db.execute(query, (newName, customerid))
            self.db.commit()
            
            return True
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False