import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5",
    database = "CompanyDb"
)

obj= mydb.cursor()
query = """
        create table student(id int primary key,
        name varchar(50),
        age int,
        place varchar(50),
        course varchar(20),
        mobile bigint,
        college varchar(50));
        """
# obj.execute(query)

values = [  (1,"Ann",22,"Tdpa","Python",987654321,"AJCE"),
            (2,"Ambu",35,"Tdpa","Python",900000000,"Luminar")
         ]

query = """
        insert into student(id,name,age,place,course,mobile,college)
        values(%s, %s, %s, %s, %s, %s, %s)
        """

# obj.executemany(query,values)
mydb.commit()


value = (3,"Anu",37,"NZ","DataScience",900110000,"Bank")
# obj.execute(query,value)
mydb.commit()


obj.execute("update student set place = 'Thodupuzha' where id = 2")
mydb.commit()

obj.execute("delete from student where id = 3")
mydb.commit()

obj.execute("select * from student")
result = obj.fetchall()
for i in result:
    print(i)


obj.close()
mydb.close()

