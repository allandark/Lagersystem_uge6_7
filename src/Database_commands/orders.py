import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="917319",
    database="lagersystem"
)

def ordersGetall():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM orders")

    myresult = mycursor.fetchall()


def ordersInsert(produktID,invoicenummer,customerid,status,mængde,lagerID):
    mycursor = mydb.cursor()

    query = "INSERT INTO orders (produktID, invoicenummer,customerid,status,mængde,lagerID) VALUES (%s, %s, %s,%s, %s, %s)"

    mycursor.execute(query, (produktID, invoicenummer, customerid,status,mængde,lagerID))
    mydb.commit()

def ordersGetbyID(OrderID):
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM orders where OrderID = %s ", (OrderID,))

    myresult = mycursor.fetchall()


def ordersGetbyProduktID(produktID):
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM orders where produktID = %s ", (produktID,))

    myresult = mycursor.fetchall()


def ordersGetbyCustomerID(customerid):
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM orders where customerid = %s ", (customerid,))

    myresult = mycursor.fetchall()


def ordersGetbylagerID(lagerID):
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM orders where lagerID = %s ", (lagerID,))

    myresult = mycursor.fetchall()



def ordersGetbyStatus(status):
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM orders where status = %s ", (status,))

    myresult = mycursor.fetchall()



def ordersGetbyinvoicenummer(invoicenummer):
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM orders where invoicenummer = %s ", (invoicenummer,))

    myresult = mycursor.fetchall()

def orderUpdateStatus(OrderID,newStatus):
    mycursor = mydb.cursor()

    query = "UPDATE orders SET status = %s WHERE OrderID = %s"

    mycursor.execute(query, (newStatus, OrderID))
    mydb.commit()

def ordercustomerview(OrderID):
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT"
                     f" orders.invoicenummer,"
                     f" produkts.navn,"
                     f" produkts.pris, "
                     f" orders.status, "
                     f" orders.mængde "
                     f"FROM orders "
                     f" join produkts on orders.produktID = produkts.produktID"
                     f" join customers on orders.customerid = customers.customerID"
                     f" where orders.customerid = %s ", (customerid,))

    myresult = mycursor.fetchall()

