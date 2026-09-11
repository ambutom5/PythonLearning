import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5",
    database = "CompanyDb"
)

obj = mydb.cursor()
query = """
        update employee set place = 'Trivandrum' where id = 1
        """
obj.execute(query)
mydb.commit()

obj.execute("select * from employee where id = 1")
result = obj.fetchone()
print(result)