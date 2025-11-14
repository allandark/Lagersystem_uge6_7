import mysql.connector

class WarehouseModel:
    
    def __init__(self, db):
        self.db = db 
    
    def GetALL(self):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM lagers")
                myresult_raw = cursor.fetchall()
                result = []
                for wh in myresult_raw:
                    result.append(WarehouseModel._tuple2Dict(wh))
                return result        
        except Exception as e:
            print("Error getting all lager:", e)
            return False
        finally:
            if conn is not None:
                conn.close()

    def GetByID(self, lagerID):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM lagers where lagerID = %s ", (lagerID,))
                myresult = cursor.fetchall()
                return WarehouseModel._tuple2Dict(myresult[0])
        except Exception as e:
            print("Error getting lagers by ID:", e)
            return False
        finally:
            if conn is not None:
                conn.close()

    def GetByName(self, navn):
        
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                cursor.execute(f"SELECT * FROM lagers where navn = %s ", (navn,))

                myresult = cursor.fetchall()
                result = []
                for wh in myresult:
                    result.append(WarehouseModel._tuple2Dict(wh))
                return result
        except Exception as e:
            print("Error getting lagers by navn:", e)
            return False
        finally:
            if conn is not None:
                conn.close()

    def Insert(self, navn):
        
        try:
            n_id = -1
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                query = "INSERT INTO lagers (navn) VALUES (%s)"
                cursor.execute(query, (navn,))
                n_id = cursor.lastrowid
            conn.commit()
            wh = {
                "id": n_id,
                "name": navn
            }            
            return wh
        except Exception as e:
            print("Error inserting Lager:", e)
            return False
        finally:
            if conn is not None:
                conn.close()

    def Update(self, id, navn):
        try:
            conn = self.db.get_connection()
            query = """
                UPDATE lagers
                SET navn = %s
                WHERE lagerID = %s
            """

            with conn.cursor() as cursor:
                cursor.execute(query, (navn, id))

            conn.commit()
            wh = {
                "id": id,
                "name": navn
            }     
            return wh
        except Exception as e:
            print(f"Error updating LagerManger: {e}")
            return False
        finally:
            if conn is not None:
                conn.close()

    def Delete(self, id):
        try:
            conn = self.db.get_connection()
            with conn.cursor() as cursor:
                query = "DELETE FROM lagers WHERE lagerID = %s"
                cursor.execute(query, (id,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting lager: {e}")
            return False
        finally:
            if conn is not None:
                conn.close()
    
    def _tuple2Dict(tuple):
        return {"id": tuple[0], "name": tuple[1]}