import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5"
)

obj = mydb.cursor()
obj.execute("SELECT VERSION()")
print(obj.fetchone())

obj.execute("SHOW DATABASES")
print(obj.fetchall())