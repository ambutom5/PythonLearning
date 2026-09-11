import mysql.connector
from datetime import datetime

from MySQL_PyCharm.EmployeeManagementCRUD.gui import department, joining_date


class Connect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Anu@mbu5",
            database = "luminar"
            )
            return self.connection
        except Exception as e:
            print(e)

class EmployeeManager(Connect):
    def post(self,**kwargs):
        try:
            self.connect = self.get_connection()
            self.cursor = self.connect.cursor()
            query = "insert into employeee (name,place,department,salary,joining_date) values(%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("Employee Added")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connect = self.get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employeee"
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            print(record)
        except Exception as e:
            print(e)

    def get_id(self,id = None):
        try:
            self.connect = self.get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employeee where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print(e)

    def retrieve(self,id = None):
        try:
            self.connect = self.get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("No Employee Found!")
            else:
                print(record)
        except Exception as e:
            print(e)

    def delete(self,id = None):
        try:
            self.connect = self.get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Employee Not Found!")
            else:
                query = "delete from employeee where id = %s"
                values = (id,)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Employee Deleted!")
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            self.connect = self.get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Employee Not Found!")
            else:
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + " = %s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update employeee set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Employee Updated!")
        except Exception as e:
            print(e)


employee_instance = EmployeeManager()
# employee_instance.post(name = "Anu",place = "Trissur",department = "ECE",salary = 70000, joining_date = datetime.today())
# employee_instance.get()
# employee_instance.get_id(id = 3)
# employee_instance.retrieve(id = 3)
# employee_instance.delete(id =3)
# employee_instance.put(id = 2,name = "Annu",place = "Trichi",department = "EEE",salary = 20000)