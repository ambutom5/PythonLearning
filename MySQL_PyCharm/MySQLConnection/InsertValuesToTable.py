import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Anu@mbu5",
    database = "CompanyDb"
)

obj = mydb.cursor()

query = """

insert into employee (id,name,place,company,age,salary) values
(1,"Ann","Kottayam","TCS",25,32000),
(2,"Meenu","Kochi","CTS",20,18000),
(3,"Ben","Palakkad","Sapiens",22,20000),
(4,"Mary","Kakkanad","Wipro",27,27000),
(5,"Kaleb","Trissur","Capegemini",30,30000)

"""

obj.execute(query)
mydb.commit()