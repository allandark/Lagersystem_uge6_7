import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="917319",
    database="lagersystem"
)

def customersGetAll():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM customers")

    myresult = mycursor.fetchall()



def customersbyId(id):
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM customers where customerid = %s ", (id,))

    myresult = mycursor.fetchall()

def customersinsert(name,Email):
    mycursor = mydb.cursor()

    query = "INSERT INTO customers (navn, Email) VALUES (%s, %s)"

    mycursor.execute(query, (name, Email))
    mydb.commit()

def customerUpdateName(customerid,newName):
    mycursor = mydb.cursor()

    query = "UPDATE customers SET navn = %s WHERE customerid = %s"

    mycursor.execute(query, (newName, customerid))
    mydb.commit()
