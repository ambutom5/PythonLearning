# multilevel
#
#
# class hospital
#     hosp name,location, contact
# dept
#     id, dept name, hod name
# patient
#     p id, name, age, place, illness, contact

class Hospital:
    def __init__(self):
        self.hospital_name = ""
        self.location = ""
        self.contact = 0
    def hospital_data(self):
        self.hospital_name = input("Enter Hospital Name: ")
        self.location = input("Enter Hospital location: ")
        self.contact = int(input("Enter Contact Number: "))
    def hospital_info(self):
        print("-------------Hospital Info---------------")
        print("Hospital Name: ",self.hospital_name)
        print("Location: ",self.location)
        print("Contact Number: ",self.contact)

class Department(Hospital):
    def __init__(self):
        self.dept_id = 0
        self.dept_name = ""
        self.hod = ""
    def department_data(self):
        obj1.hospital_data()
        self.dept_id = int(input("Enter Dept. Id: "))
        self.dept_name = input("Enter Dept. Name: ")
        self.hod = input("Enter HOD Name: ")
    def department_info(self):
        obj1.hospital_info()
        print("-------------------Dept Info--------------------")
        print("Department ID: ",self.dept_id)
        print("Department Name: ",self.dept_name)
        print("HOD: ",self.hod)

class Patient(Department):
    def __init__(self):
        self.patient_id = 0
        self.patient_name = ""
        self.age = 0
        self.place = ""
        self.illness = ""
        self.pcontact = 0
    def patient_data(self):
        obj1.department_data()
        self.patient_id = int(input("Enter Patient Id: "))
        self.patient_name = input("Enter Patient Name: ")
        self.age = int(input("Enter Patient Age: "))
        self.place = input("Enter Patient Place: ")
        self.illness = input("Enter Patient Illness: ")
        self.pcontact = int(input("Enter Patient Contact No: "))
    def patient_info(self):
        obj1.department_info()
        print("-------------Patient Info---------------")
        print("Patient Id: ",self.patient_id)
        print("Patient Name: ",self.patient_id)
        print("Age: ",self.age)
        print("Place: ",self.place)
        print("Illness: ",self.illness)
        print("Contact: ",self.pcontact)

obj1 = Patient()
obj1.patient_data()
obj1.patient_info()

