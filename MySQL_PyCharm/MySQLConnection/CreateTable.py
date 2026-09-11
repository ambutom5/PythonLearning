import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5",
    database = "CompanyDb"
)

obj = mydb.cursor()

query = """
        create table Employee(
        id int primary key,
        name varchar(100),
        place varchar(200),
        company varchar(200),
        age int,//
        salary int)
"""

obj.execute(query)
print("Table created Successfully!")