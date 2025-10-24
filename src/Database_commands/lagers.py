import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="917319",
    database="lagersystem"
)
def lagersgetALL():

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM lagers")

    myresult = mycursor.fetchall()


def lagersGetAllbyLagerID(lagerID):

    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM lagers where lagerID = %s ", (lagerID,))

    myresult = mycursor.fetchall()


def lagersGetAllbyLagerNavn(navn):

    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM lagers where navn = %s ", (navn,))

    myresult = mycursor.fetchall()


def lagerinstert(navn):
    mycursor = mydb.cursor()

    query = "INSERT INTO lagers (navn) VALUES (%s)"

    mycursor.execute(query, (navn,))
    mydb.commit()