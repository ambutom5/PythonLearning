import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5",
    database = "CompanyDb"
)

obj = mydb.cursor()
obj.execute("select * from employee")
employee = obj.fetchone()
print(employee)