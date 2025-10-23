import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="917319",
    database="lagersystem"
)

def productsGetAll():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM produkts")

    myresult = mycursor.fetchall()


def productsGetbyId(id):
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM produkts where produktID = %s ", (id,))

    myresult = mycursor.fetchall()


def productsGetbyPrise(pris):
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM produkts where pris = %s ", (pris,))

    myresult = mycursor.fetchall()


def insertproduct(name, price):

    mycursor = mydb.cursor()

    query = "INSERT INTO produkts (navn, pris) VALUES (%s, %s)"

    mycursor.execute(query, (name, price))
    mydb.commit()

def productsGetbyName(name):
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM produkts where navn = %s ", (name,))

    myresult = mycursor.fetchall()



