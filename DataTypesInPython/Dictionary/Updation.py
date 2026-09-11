student = {"Name":"Anu",
           "Age":30,
           "Gender":"Female",
           "Course":"Python Full Stack",
           "Skills":["Python","Django","HTML"]}

print(student)
student["Mobile"] = 9496624324
print(student)
print(student["Mobile"])

student["Name"] = "Anupriya"
print(student)
print(student["Name"])

del student["Gender"]
print(student)

student.clear()
print(student)

del student
print(student)