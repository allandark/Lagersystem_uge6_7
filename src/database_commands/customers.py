import mysql.connector


class CustomersModel:

    def __init__(self, db):
        self.db = db
        
    def GetAll(self):
        
        try:
            with self.db.cursor() as cursor:
                cursor.execute("SELECT * FROM customers")

                myresult = cursor.fetchall()
                customers = []
                for c in myresult:
                    customers.append(CustomersModel._toTuple(c))
                return customers                
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False


    def GetById(self, id):

        try:
            with self.db.cursor() as cursor:
                cursor.execute(f"SELECT * FROM customers where customerid = %s ", (id,))
                myresult = cursor.fetchall()        
                return CustomersModel._toTuple(myresult[0])

        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False
        
    def Insert(self, name, email):

        try:
            n_id = -1
            with self.db.cursor() as cursor:
                query = "INSERT INTO customers (navn, Email) VALUES (%s, %s)"

                cursor.execute(query, (name, email))
                n_id = cursor.lastrowid
            self.db.commit()
            customer = {
                "id": n_id,
                "name": name,
                "email": email
            }
            return customer
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False

    def Update(self, customerid, name, email):
        try:
            query = """
                            UPDATE customers
                            SET navn = %s, Email = %s
                            WHERE customerid = %s
                        """
            with self.db.cursor() as cursor:
                cursor.execute(query, (name, email, customerid))
            self.db.commit()
            customer = {
                "id": customerid,
                "name": name,
                "email": email
            }
            return customer
        except Exception as e:
            print(f"Customer update error: {e}")
            return False

    def Delete(self, id):
        try:
            with self.db.cursor() as cursor:
                query = "DELETE FROM customers WHERE customerid = %s"
                cursor.execute(query, (id,))
            self.db.commit()
            return True
        except Exception as e:
            print(f"Error deleting customers: {e}")
            return False

    def _toTuple(tuple):
        return {
            "id": tuple[0],
            "name": tuple[1],
            "email": tuple[2]
        }
