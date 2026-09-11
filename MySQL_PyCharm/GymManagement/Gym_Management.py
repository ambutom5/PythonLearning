import mysql.connector
from datetime import  datetime

class DbConnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Anu@mbu5",
                database = "gym_db"
            )
            return self.connection
        except Exception as e:
            return None

class GymMemberManager(DbConnect):
    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            self.cursor.execute("select * from member")
            records = self.cursor.fetchall()
            # for row in records:
                # print(row)
            return records
        except Exception as e:
            # print(e)
            return []

    def post(self,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "insert into member(name,place,mobile,plan,fee,joined_on) values(%s,%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("New Member Added!")
        except Exception as e:
            print(e)

    def get_id(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from member where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            if record == None:
                # print("Member Not Found!")
                return None
            else:
                # print(record)
                return record
        except Exception as e:
            print(e)

    def delete(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Member Not Found!")
            else:
                query = "delete from member where id = %s"
                values = (id,)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Member Deleted!")
        except Exception as e:
            print(e)

    def put(self,id=None,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if id == None:
                print("Member Not Found!")
            else:
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + " = %s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update member set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Member Updated!")
        except Exception as e:
            print(e)

    def get_object(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from member where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None

    def retrieve(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            records = self.get_object(id = id)
            if records == None:
                print("Member Not Found")
            else:
                print(records)

        except Exception as e:
            print(e)

    def delete1(self,id = None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            records = self.get_object(id = id)
            if records == None:
                print("Member Not Found")
            else:
                query = "delete from member where id = %s"
                values = (id,)
                self.cursor.execute(query, values)
                self.connect.commit()
                print("Member deleted!")
        except Exception as e:
            print(e)

    def put1(self,id = None,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_object(id = id)
            if record == None:
                print("Member Not Found")
            else:
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + " = %s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update member set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Member Updated!")

        except Exception as e:
            print(e)

connection_instance = DbConnect()
# print(connection_instance.get_connection())

member_instance = GymMemberManager()
# member_instance.get()
# member_instance.post(name = "Anu",place = "Trissur",mobile = "987654321",plan = "3month",fee = 500,joined_on = datetime.today())
# member_instance.post(name = "Ambu",place = "Kochi",mobile = "987600321",plan = "6month",fee = 1000,joined_on = datetime.today())
# member_instance.post(name = "Linto",place = "Kakkanad",mobile = "900654321",plan = "3month",fee = 500,joined_on = datetime.today())
# member_instance.post(name = "Anju",place = "Aluva",mobile = "987654300",plan = "1month",fee = 100,joined_on = datetime.today())
# member_instance.post(name = "Manu",place = "Trissur",mobile = "987004321",plan = "1year",fee = 1500,joined_on = datetime.today())
# member_instance.get()
# member_instance.get_id(id =4)
# member_instance.delete(id = 6)
# member_instance.put(id = 3, plan = "1year", place = "Kochi")
# member_instance.retrieve(id = 3)
# member_instance.delete1(id = 7)

# member_instance.put1(id=10,name="Krishna Priya",place = "Alappuzhaaa",mobile = "900007654")