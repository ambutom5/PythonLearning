import mysql.connector

class BloodDonorManager:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Anu@mbu5",
            database = "blood_db"
        )
        print("Connection Success")
        self.cursor = self.connection.cursor()

    def post(self,**kwargs):
        query = "insert into bdonor(name,age,bld_grp,place) values (%s,%s,%s,%s)"
        values = [v for v in kwargs.values()]
        self.cursor.execute(query,values)
        self.connection.commit()
        print("Donor Added!")

    def get(self):
        self.cursor.execute("select * from bdonor")
        result = self.cursor.fetchall()
        for row in result:
            print(row)

    def gett(self, id = None):
        query = "select * from bdonor where id = %s"
        values = (id,)
        self.cursor.execute(query,values)
        result = self.cursor.fetchone()
        return result

    def delete(self,id = None):
        record = donor_instance.gett(id = id)
        if record == None:
            print("No such donor!")
        else:
            query = "delete from bdonor where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Donor Deleted!")

    def patch(self,id = None):
        record = donor_instance.gett(id = id)
        if record == None:
            print("No such donor!")
        else:
            query = "update bdonor set place = 'Rajagiri' where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Donor Updated!")

    def getid(self,id = None):
        query = "select * from bdonor where id = %s"
        values = (id,)
        self.cursor.execute(query,values)
        result = self.cursor.fetchone()
        return result

    def deleteid(self,id = None):
        result = donor_instance.getid(id = id)
        if result == None:
            print("No Such Donor")
        else:
            query = "delete from bdonor where id = %s"
            values = (id,)
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Donor Deleted")


    def put(self,id = None, **kwargs):
        try:
            record = donor_instance.getid(id = id)
            if record == None:
                print("Donor Not Found")
            else:
                self.cursor = self.connection.cursor()
                placeholder = ", ".join([f"{k} = %s" for k in kwargs.keys()])
                query = f"update bdonor set {placeholder} where id = %s"
                values = [v for v in kwargs.values()]
                values.append(id)
                # values = list(kwargs.values()) + [id]
                print("Query:", query)
                print("Values:", values)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Donor Updated!")
        except Exception as e:
            print("Error!",e)


donor_instance = BloodDonorManager()
# donor_instance.post(name = "Ambu",age = 30,bld_grp = "A+",place = "Kochi")
# donor_instance.post(name = "Anu",age = 35,bld_grp = "B+",place = "Trissur")
# donor_instance.post(name = "Leo",age = 4,bld_grp = "A+",place = "Kakkanad")
# donor_instance.gett(id = 3)

# donor_instance.delete(id = )
# donor_instance.patch(id = 3)
# donor_instance.getid(id = 2)
# donor_instance.deleteid(id = 5)

donor_instance.put(id = 4,name = "Manu",age  = 40)