import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5"
)

mycursor = mydb.cursor()
# mycursor.execute("Create database CompanyDb")
# print("DB Created Successfully!")
mycursor.execute("show databases")
print(mycursor.fetchall())