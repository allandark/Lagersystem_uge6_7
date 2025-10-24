import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="917319",
    database="lagersystem"
)

def lagerMangergetALL():

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM lager_manger")

    myresult = mycursor.fetchall()



def lagerMangerGetALlbyProductID(produktID):

    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM lager_manger where produktID = %s ", (produktID,))


    myresult = mycursor.fetchall()


def lagerMangerGetAllbyLagerID(lagerID):

    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM lager_manger where lagerID = %s ", (lagerID,))

    myresult = mycursor.fetchall()


def lagerMangerInsert(lagerID,produktID,antal):
    mycursor = mydb.cursor()

    query = "INSERT INTO lager_manger (lagerID, produktID,antal) VALUES (%s, %s, %s)"

    mycursor.execute(query, (lagerID, produktID,antal))
    mydb.commit()