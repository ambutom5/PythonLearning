import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5",
    database = "CompanyDb"
)

obj = mydb.cursor()
query = """
        delete from employee where id = 4
        """
obj.execute(query)
mydb.commit()

obj.execute("select * from employee")
result = obj.fetchall()
print(result)
