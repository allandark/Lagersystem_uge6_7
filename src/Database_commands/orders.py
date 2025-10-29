import mysql.connector

class OrdersModel:
    def __init__(self,db):
        self.db = db
    
    def GetAll(self):
        try:
            self.db.execute("SELECT * FROM orders")

            myresult = self.db.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting all orders:", e)
            return False


    def Insert(self, produktID,invoicenummer,customerid,status,mængde,lagerID):
        
        try:
            query = "INSERT INTO orders (produktID, invoicenummer,customerid,status,mængde,lagerID) VALUES (%s, %s, %s,%s, %s, %s)"

            self.db.execute(query, (produktID, invoicenummer, customerid,status,mængde,lagerID))
            self.db.commit()
            return True
        except Exception as e:
            print("Error inserting orders:", e)
            return False
    def GetByID(self, OrderID):
        
        try:
            self.db.execute(f"SELECT * FROM orders where OrderID = %s ", (OrderID,))

            myresult = self.db.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting orders by orderID:", e)
            return False

    def GetByProductID(self, produktID):
        
        try:
            self.db.execute(f"SELECT * FROM orders where produktID = %s ", (produktID,))

            myresult = self.db.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting orders by productID:", e)
            return False


    def GetByCustomerID(self, customerid):
        
        try:
            self.db.execute(f"SELECT * FROM orders where customerid = %s ", (customerid,))

            myresult = self.db.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting orders by customerID:", e)
            return False

    def GetByWarehouseID(self, lagerID):
        
        try:
            self.db.execute(f"SELECT * FROM orders where lagerID = %s ", (lagerID,))

            myresult = self.db.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting orders by lagerID:", e)
            return False


    def GetbyStatus(self, status):
        
        try:
            self.db.execute(f"SELECT * FROM orders where status = %s ", (status,))

            myresult = self.db.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting orders by status:", e)
            return False


    def GetByInvoiceNumber(self, invoicenummer):
        
        try:
            self.db.execute(f"SELECT * FROM orders where invoicenummer = %s ", (invoicenummer,))

            myresult = self.db.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting orders by invoicenumber:", e)
            return False
        
    def UpdateStatus(self, OrderID,newStatus):
        
        try:
            query = "UPDATE orders SET status = %s WHERE OrderID = %s"

            self.db.execute(query, (newStatus, OrderID))
            self.db.commit()
        
            return True
        except Exception as e:
            print("Error updateing orders status:", e)
            return False
        
    def OrderCustomerView(self, customerid):
        
        try:
            self.db.execute(f"SELECT"
                     f" orders.invoicenummer,"
                     f" produkts.navn,"
                     f" produkts.pris, "
                     f" orders.status, "
                     f" orders.mængde "
                     f"FROM orders "
                     f" join produkts on orders.produktID = produkts.produktID"
                     f" join customers on orders.customerid = customers.customerID"
                     f" where orders.customerid = %s ", (customerid,))

            myresult = self.db.fetchall()
        
            return myresult
        except Exception as e:
            print("Error getting orders in customerview:", e)
            return False
