import mysql.connector

class lager_mangerModel:
    
    def __init__(self, db):
        self.db = db
    

    def lagerMangergetALL(self):
        
        try:
            self.db.execute("SELECT * FROM lager_manger")

            myresult = self.db.fetchall()
        
            return myresult
        
        except Exception as e:
            print("Error getting LagerManger:", e)
            return False
        
    def lagerMangerGetALlbyProductID(self,produktID):
        
        try:
            self.db.execute(f"SELECT * FROM lager_manger where produktID = %s ", (produktID,))


            myresult = self.db.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting LagerManger by produktID:", e)
            return False
        
    def lagerMangerGetAllbyLagerID(self,lagerID):
        
        try:
            self.db.execute(f"SELECT * FROM lager_manger where lagerID = %s ", (lagerID,))

            myresult = self.db.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting LagerManger by id:", e)
            return False
        
    def lagerMangerInsert(self,lagerID,produktID,antal):
        
        try:
            query = "INSERT INTO lager_manger (lagerID, produktID,antal) VALUES (%s, %s, %s)"

            self.db.execute(query, (lagerID, produktID,antal))
            self.db.commit()
            return True
        except Exception as e:
            print("Error inserting LagerManger:", e)
            return False