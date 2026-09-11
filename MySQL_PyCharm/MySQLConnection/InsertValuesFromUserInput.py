import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5",
    database = "CompanyDb"
)

obj = mydb.cursor()

id = int(input("Enter the Id: "))
name = input("Enter name: ")
place = input("Enter place: ")
company = input("Enter company: ")
age = int(input("Enter the age: "))
salary = int(input("Enter the salary: "))

values = (id,name,place,company,age,salary)

query = """
        insert into employee (id,name,place,company,age,salary) values 
        (%s, %s, %s, %s, %s, %s)
        """
obj.execute(query,values)

mydb.commit()

obj.execute("select * from employee")
result = obj.fetchall()
for i in result:
    print(i)