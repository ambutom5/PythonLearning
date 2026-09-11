import mysql.connector
from datetime import datetime

class ConnectionClass:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Anu@mbu5",
                database = "company_db"
            )
            return self.connection
        except Exception as e:
            return  None

class EmployeeManager(ConnectionClass):

    def post(self,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "insert into employee(name,place,mobile,email,department,salary,joining_date) values(%s,%s,%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("Employee added Successfully!")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employee"
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            # for row in record:
            #     print(row)
            return record
        except Exception as e:
            # print(e)
            return []


    def get_object(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employee where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            # print(record)
            return record
        except Exception as e:
            print(e)


    def retrieve(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_object(id = id)
            if record == None:
                print("Member Not Found!")
            else:
                print(record)
        except Exception as e:
            print(e)

    def delete(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_object(id = id)
            if record == None:
                print("Member Not Found!")
            else:
                query = "delete from employee where id = %s"
                values = (id,)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Member Deleted!")
        except Exception as e:
            print(e)

    def put(self,id = None,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_object(id = id)
            if record == None:
                print("Member Not Found!")
            else:
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + " = %s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update employee set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Employee Updated!")
        except Exception as e:
            print(e)

employee_instance = EmployeeManager()
# employee_instance.post(name = "Anu", place = "Pala", mobile = "900087654", email = "anu19@gmail.com",department = "ECE",salary = 50000, joining_date = datetime.today())
# employee_instance.post(name = "Ambu", place = "Kochi", mobile = "911087654", email = "ambu19@gmail.com",department = "IT",salary = 40000, joining_date = datetime.today())
# employee_instance.post(name = "Manu", place = "Trissur", mobile = "922087654", email = "manu19@gmail.com",department = "ECE",salary = 30000, joining_date = datetime.today())
# employee_instance.post(name = "Krishna", place = "Pattanamtitta", mobile = "933087654", email = "krish19@gmail.com",department = "Mech",salary = 80000, joining_date = datetime.today())
# employee_instance.post(name = "Dany", place = "Kottayam", mobile = "944087654", email = "dany19@gmail.com",department = "EEE",salary = 20000, joining_date = datetime.today())

# employee_instance.get()
# employee_instance.get_object(id = 3)
# employee_instance.retrieve(id = 3)
# employee_instance.delete(id = 5)

# employee_instance.put(id = 5, name = "KrishnaPriya", place = "PTA", salary = 3000)
