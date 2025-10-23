import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="917319",
    database="lagersystem"
)


def adminGetAll():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM admin")

    myresult = mycursor.fetchall()



def adminGetbyId(id):
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT * FROM admin where adminid = %s ", (id,))

    myresult = mycursor.fetchall()


def admininsert(name,password):
    mycursor = mydb.cursor()

    query = "INSERT INTO admin (navn, adminpassword) VALUES (%s, %s)"

    mycursor.execute(query, (name, password))
    mydb.commit()

def adminupdateName(adminid,newName):
    mycursor = mydb.cursor()

    query = "UPDATE admin SET navn = %s WHERE adminid = %s"

    mycursor.execute(query, (newName, adminid))
    mydb.commit()

def adminupdatePassword(adminid,adminpassword):
    mycursor = mydb.cursor()

    query = "UPDATE admin SET adminpassword = %s WHERE adminid = %s"

    mycursor.execute(query, (adminpassword, adminid))
    mydb.commit()
