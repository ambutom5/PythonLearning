import mysql.connector
from datetime import datetime

class BloodDonorManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Anu@mbu5",
            database = "luminar"
        )
        self.cursor = self.connection.cursor()
        # print("Connection Success!")

    def post(self,**kwargs):
        try:
            # query = "insert into donor(name,phone,city,last_donation) values(%s,%s,%s,%s)"
            query = "insert into donor(name,blood_group,phone,city,last_donation) values (%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Donor Added Successfully!")
        except Exception as e:
            print(e)

    def get(self):
        self.cursor = self.connection.cursor()
        query = "select * from donor"
        self.cursor.execute(query)
        records = self.cursor.fetchall()


    def getid(self,id = None):
        try:
            query = "select * from donor where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            print("Ferror",e)

    def delete(self,id = None):
        try:
            record = self.getid(id=id)
            if record == None:
                print("Donor Not Found!")
            else:
                query = "delete from donor where id = %s"
                values = (id,)
                self.cursor.execute(query,values)
                self.connection.commit()
        except Exception as e:
            print(e)


    def put(self,id= None,**kwargs):
        try:
            record = self.getid(id = id)
            if record == None:
                print("Donor Not Found!")
            else:
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + " = %s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update donor set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                print(query)
                print(values)
                self.cursor.execute(query,values)
                self.connection.commit()
        except Exception as e:
            print("Error",e)

donor_instance = BloodDonorManager()
# donor_instance.post(name = "Ambu", phone = "987654320",city = "Kochi",last_donation = datetime.today())
# donor_instance.post(name = "Manu", blood_group = "O+", phone = "980859320",city = "Trissur",last_donation = datetime.today())
# donor_instance.post(name = "Mannu", blood_group = "O-", mobile = "980809320",city = "Trissur",last_donation = datetime.today())
# donor_instance.delete(id = 7)
donor_instance.put(id = 8, name = "Bhanu", phone = "110809320", city = "Trichi")

