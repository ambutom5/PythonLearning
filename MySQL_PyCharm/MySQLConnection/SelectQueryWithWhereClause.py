import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5",
    database = "CompanyDb"
)

obj = mydb.cursor()
obj.execute("select * from employee where id = 3")
employee = obj.fetchone()
print(employee)

obj.execute("select * from employee where company = 'TCS'")
result = obj.fetchall()
for emp in result:
    print(emp)

obj.execute("select * from employee where place = 'Kochi'")
result = obj.fetchall()
for row in result:
    print(row)

obj.execute("select * from employee where place = 'Kochi'")
result = obj.fetchall()
print(result)
