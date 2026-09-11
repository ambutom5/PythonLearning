import mysql.connector
from  datetime import datetime

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
            record = self.cursor.fetchall()
            for row in record:
                print(row)
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
            # print(record)
            return record

        except Exception as e:
            print(e)

    def post(self,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "insert into member(name,place,mobile,plan,fee,joined_on) values(%s,%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("Member Added!")
        except Exception as e:
            print(e)

    def delete(self,id= None):
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

    def put(self,id= None,**kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            record = self.get_id(id = id)
            if record == None:
                print("Member Not Found!")
            else:
                placeholder = ", ".join([f"{k} = %s" for k in kwargs.keys()])
                query = f"update member set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Member Updated!")
        except Exception as e:
            print(e)


member_instance = GymMemberManager()

# member_instance.post(name = "Anjana",place = "Aluva",mobile = "900008765",plan = "1month",fee =100,joined_on = datetime.today())
# member_instance.post(name = "Ansiya",place = "Ernakulam",mobile = "901108765",plan = "2month",fee =200,joined_on = datetime.today())
# member_instance.post(name = "Nimisha",place = "Kochi",mobile = "900000760",plan = "3month",fee =300,joined_on = datetime.today())
# member_instance.post(name = "Krishna",place = "Palakkad",mobile = "907708765",plan = "6month",fee =600,joined_on = datetime.today())

# member_instance.get()
# member_instance.get_id(id = 5)
# member_instance.delete(id =5)

member_instance.put(id = 7,name = "Anju",place = "Aluvaa",mobile = "910008765",plan = "2month",fee =200)
