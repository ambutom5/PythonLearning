import  mysql.connector

class Connect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Anu@mbu5",
                database="luminar"
            )
            return self.connection
        except Exception as e:
            return None

class Student(Connect):
    def post(self,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "insert into studentt (id,name,age,place) values (%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("Student Added!")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from studentt"
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            for row in record:
                print(row)
        except Exception as e:
            print(e)

    def get_id(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from studentt where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record

        except Exception as e:
            return None

    def retrieve(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Student Not Found!")
            else:
                print(record)

        except Exception as e:
            print(e)

    def delete(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Student Not Found!")
            else:
                query = "delete from studentt where id = %s"
                values = (id,)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Student Deleted!")
        except Exception as e:
            print(e)

    def put(self,id = None,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Student Not Found!")
            else:
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + " = %s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update studentt set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Student Updated")
        except Exception as e:
            print(e)



student_instance = Student()
# student_instance.post(id = 6,name = "Mannu",age = 30,place = "Tirur")
# student_instance.get()
# student_instance.get_id(id = 5)
# student_instance.retrieve(id = 3)
# student_instance.delete(id = 6)
student_instance.put(id = 5,name = "Mannu",age = 30,place = "Tirur")






