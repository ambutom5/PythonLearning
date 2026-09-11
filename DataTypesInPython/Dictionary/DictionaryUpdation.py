student = {"Name":"Ambu",
           "Age":35,}

print(student["Name"])
print(student["Age"])
print(student)

student["Name"]="Ambily"                        # Updating Existing Key-Value
student["RollNo"] = 5                           # Defining new Key-Value
print(student)

student.update({"Name":"Amy"})                  # Updating Existing Key-Value
print(student)

student.update({"College":"AJCE"})              # Defining new Key-Value
print(student)

del student["Age"]
print(student)

student.clear()
print(student)

del student
# print(student)

