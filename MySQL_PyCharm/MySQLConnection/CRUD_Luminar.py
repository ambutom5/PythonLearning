import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5",
    database = "Luminar"
)

obj = mydb.cursor()

query = """
        create table studentt (
        id int primary key,
        name varchar(50),
        age int,place varchar(100))
        """
obj.execute(query)
mydb.commit()

values = (4,"Linto",39,"Kakkanad")

mylist =    [
                (1,"Ambu",35,"Kochi"),
                (2,"Anu",38,"NZ"),
                (3,"Leo",4,"Kakkanad")
            ]

query = "insert into studentt (id,name,age,place) values (%s,%s,%s,%s)"

obj.executemany(query,mylist)
obj.execute(query,values)

obj.execute("update studentt set place = 'New Zealand' where id = 2")
obj.execute("delete from studentt where id = 4")

mydb.commit()

obj.execute("select * from studentt")
result = obj.fetchall()
for i in result:
    print(i)

