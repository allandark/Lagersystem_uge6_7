import mysql.connector


class CustomersModel:

    def __init__(self, db):
        self.db = db
        
    def GetAll(self):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
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
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM customers where customerid = %s ", (id,))
                myresult = cursor.fetchall()    
                if myresult == []:
                    return []
                else:    
                    return CustomersModel._toTuple(myresult[0])

        except Exception as e:
            print("Error checking if customer exist by id:", e)
            return False
    
    def GetByEmail(self, email):

        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM customers where email = %s ", (email,))
                myresult = cursor.fetchall()
                if myresult == []:
                    return []
                else:      
                    return CustomersModel._toTuple(myresult[0])

        except Exception as e:
            print("Error checking if customer exist by email:", e)
            return False
        
    def Insert(self, name, email):

        try:
            n_id = -1
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                query = "INSERT INTO customers (navn, Email) VALUES (%s, %s)"

                cursor.execute(query, (name, email))
                n_id = cursor.lastrowid
            conn.commit()
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
            conn = self.db.get_connection()
            query = """
                            UPDATE customers
                            SET navn = %s, Email = %s
                            WHERE customerid = %s
                        """
            with conn.cursor() as cursor:
                cursor.execute(query, (name, email, customerid))
            conn.commit()
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
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                query = "DELETE FROM customers WHERE customerid = %s"
                cursor.execute(query, (id,))
            conn.commit()
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
