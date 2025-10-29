import mysql.connector

class AdminModel:
    
    def __init__(self, db):
        self.db = db
        
    def GetAll(self):
        
        try:
            with self.db.cursor() as cursor:
                cursor.execute("SELECT * FROM admin")
                myresult = cursor.fetchall()
                results = [] 
                for u in myresult:
                    results.append(AdminModel._TupleToDict(u))
                return results
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False


    def GetById(self, id):
        
        try:
            with self.db.cursor() as cursor:
                cursor.execute(f"SELECT * FROM admin where adminid = %s ", (id,))
                myresult = cursor.fetchall()
                user = AdminModel._TupleToDict(myresult)
                return user
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False
        
    def Insert(self, name, password_hash):
        
        try:
            n_id = -1
            with self.db.cursor() as cursor:
                query = "INSERT INTO admin (navn, adminpassword) VALUES (%s, %s)"
                cursor.execute(query, (name, password_hash))
                n_id = cursor.lastrowid
            self.db.commit()
            return {
                "id": n_id,
                "name": name,
                "password_hash": password_hash
            }
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False
        
    def Update(self, admin_id, name, password_hash):
        try:
            with self.db.cursor() as cursor:
                query = """
                    UPDATE admin
                    SET navn = %s, adminpassword = %s                    
                    WHERE adminid = %s
                """
                cursor.execute(query, (name, password_hash, admin_id))
            self.db.commit()

            return {
                "id": admin_id,
                "name": name,
                "password_hash": password_hash
            }
        except Exception as e:
            print(f"Error updating admin: {e}")
            return False

    def UpdateName(self, admin_id, new_name):
        
        try:
            with self.db.cursor() as cursor:
                query = "UPDATE admin SET navn = %s WHERE adminid = %s"
                cursor.execute(query, (new_name, admin_id))
            self.db.commit()
            return True
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False
        
    def UpdatePassword(self,admin_id, password_hash):
        
        try:
            with self.db.cursor() as cursor:
                query = "UPDATE admin SET adminpassword = %s WHERE adminid = %s"
                cursor.execute(query, (password_hash, admin_id))
            self.db.commit()
            return True
        except Exception as e:
            print("Error checking if product exist by id:", e)
            return False

    def Delete(self, admin_id):
        try:
            with self.db.cursor() as cursor:
                query = "DELETE FROM admin WHERE adminid = %s"
                cursor.execute(query, (admin_id,))
            return True
        except Exception as e:
            print(f"Error deleting admin: {e}")
            return False


    def _TupleToDict(tuple):        
            return {
                "id": tuple[0],
                "name": tuple[1],
                "password_hash": tuple[2]
            }
        