import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5"
)

if mydb.is_connected():
    print("MySQL_PyCharm Connection Success")