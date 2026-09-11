import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5",
    database = "CompanyDb"
)

obj = mydb.cursor()
query = "select * from employee"
obj.execute(query)

result = obj.fetchall()
print(result)

for emp in result:
    print(emp)
