import mysql.connector
import datetime


class BloodDonorManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Anu@mbu5",
            database="blood_db"
        )
        print("Connected Successfully")

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = "insert into donor(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connection.commit()
            print("Donor Added Successfully!")
        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()
            self.cursor.execute("select * from donor")
            records = self.cursor.fetchall()
            # for data in records:
            #     print(data)
            return records
        except Exception as e:
            # print(e)
            return []

    def retrieve(self, id=None):
        try:
            record = donor_instance.get_object(id = id)
            print(record)
            if record == None:
                print("Donor Not Found!")
        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record = donor_instance.get_object(id = id)
            if record == None:
                print("Donor Not Found!")
            else:
                query = "delete from donor where id = %s"
                values = (id,)
                self.cursor.execute(query, values)
                self.connection.commit()
                print("Donor Deleted Successfully!")

        except Exception as e:
            print(e)

    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from donor where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None

    def put(self,id = None, **kwargs):
        try:
            record = donor_instance.get_object(id = id)
            if record == None:
                print("Donor Not Found")
            else:
                self.cursor = self.connection.cursor()
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + " = %s, "
                placeholder = placeholder.rstrip(", ")
                print(placeholder)
                query = f"update donor set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                print(query)
                print(values)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Donor Updated!")
        except Exception as e:
            print("Error!",e)



donor_instance = BloodDonorManager()
# donor_instance.post(name = "Ambu",blood_group = "A+",phone = "987654321",city = "Kakkanad",last_donation = datetime.datetime.today())
# donor_instance.post(name = "Anu",blood_group = "A+",phone = "987654310",city = "Kakkanad",last_donation = datetime.datetime.today())
# donor_instance.post(name = "Annu",blood_group = "O+",phone = "987654180",city = "Kakkanad",last_donation = datetime.datetime.today())
# donor_instance.post(name = "Manu",blood_group = "B+",phone = "987154380",city = "Kochi",last_donation = datetime.datetime.today())

# donor_instance.get()
# donor_instance.retrieve(id = 15)
# donor_instance.delete(id = 15)

# donor_instance.put(id = 10,name = "Mannu",city = "Palakkad",blood_group = "O+")




