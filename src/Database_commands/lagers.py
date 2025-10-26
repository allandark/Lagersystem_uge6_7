import mysql.connector

class lagermodel:
    
    def __init__(self, db):
        self.db = db 
    
    def lagersgetALL(self):
        
        try:
            self.db.execute("SELECT * FROM lagers")

            myresult = self.db.fetchall()
            
            return myresult
        except Exception as e:
            print("Error getting all lager:", e)
            return False

    def lagersGetAllbyLagerID(self, lagerID):
        
        try:
            self.db.execute(f"SELECT * FROM lagers where lagerID = %s ", (lagerID,))

            myresult = self.db.fetchall()
            
            return myresult
        except Exception as e:
            print("Error getting lagers by ID:", e)
            return False

    def lagersGetAllbyLagerNavn(self, navn):
        
        try:
            self.db.execute(f"SELECT * FROM lagers where navn = %s ", (navn,))

            myresult = self.db.fetchall()
            
            return myresult
        except Exception as e:
            print("Error getting lagers by navn:", e)
            return False

    def lagerinstert(self, navn):
        
        try:
            query = "INSERT INTO lagers (navn) VALUES (%s)"

            self.db.execute(query, (navn,))
            self.db.commit()
            
            return True
        except Exception as e:
            print("Error inserting Lager:", e)
            return False