import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5",
    database = "CompanyDb"
)

obj = mydb.cursor()

mylist = [  (6,"Annu","Ktm","Infosys",25,40000),
            (7,"Bhanu","TN","TCS",35,55000)
         ]
query = """
        insert into employee (id,name,place,company,age,salary) 
        values (%s, %s, %s, %s, %s, %s)
"""

obj.executemany(query,mylist)
mydb.commit()