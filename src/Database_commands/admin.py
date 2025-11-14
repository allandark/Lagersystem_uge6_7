import mysql.connector

class AdminModel:
    
    def __init__(self, db):
        self.db = db
        
    def GetAll(self):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM admin")
                myresult = cursor.fetchall()
                results = [] 
                for u in myresult:
                    results.append(AdminModel._TupleToDict(u))
                return results
        except Exception as e:
            print("Error Getting all admin users:", e)
            return False
        finally:
            if conn is not None:
                conn.close()


    def GetById(self, id):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM admin where adminid = %s ", (id,))
                myresult = cursor.fetchall()
                user = AdminModel._TupleToDict(myresult[0])
                return user
        except Exception as e:
            print(f"Error checking if admin exist by id({id}):", e)
            return False
        finally:
            if conn is not None:
                conn.close()
    def Insert(self, name, password_hash):
        
        try:
            n_id = -1
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                query = "INSERT INTO admin (navn, adminpassword) VALUES (%s, %s)"
                cursor.execute(query, (name, password_hash))
                n_id = cursor.lastrowid
            conn.commit()
            return {
                "id": n_id,
                "name": name,
                "password_hash": password_hash
            }
        except Exception as e:
            print("Error inserting into db:", e)
            return False
        finally:
            if conn is not None:
                conn.close()
        
    def Update(self, admin_id, name, password_hash):
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                query = """
                    UPDATE admin
                    SET navn = %s, adminpassword = %s                    
                    WHERE adminid = %s
                """
                cursor.execute(query, (name, password_hash, admin_id))
            conn.commit()

            return {
                "id": admin_id,
                "name": name,
                "password_hash": password_hash
            }
        except Exception as e:
            print(f"Error updating admin: {e}")
            return False
        finally:
            if conn is not None:
                conn.close()

    def UpdateName(self, admin_id, new_name):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                query = "UPDATE admin SET navn = %s WHERE adminid = %s"
                cursor.execute(query, (new_name, admin_id))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error updating admin name by id({admin_id}):", e)
            return False
        finally:
            if conn is not None:
                conn.close()
        
    def UpdatePassword(self,admin_id, password_hash):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                query = "UPDATE admin SET adminpassword = %s WHERE adminid = %s"
                cursor.execute(query, (password_hash, admin_id))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error updating admin password by id({admin_id}):", e)
            return False
        finally:
            if conn is not None:
                conn.close()

    def Delete(self, admin_id):
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                query = "DELETE FROM admin WHERE adminid = %s"
                cursor.execute(query, (admin_id,))
            return True
        except Exception as e:
            print(f"Error deleting admin({admin_id}): {e}")
            return False
        finally:
            if conn is not None:
                conn.close()


    def _TupleToDict(tuple):        
            return {
                "id": tuple[0],
                "name": tuple[1],
                "password_hash": tuple[2]
            }
        