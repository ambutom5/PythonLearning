student = {"Name":"Anu",
           "Age":30,
           "Gender":"Female",
           "Course":"Python Full Stack",
           "Skills":["Python","Django","HTML"]}


for i in student:                               # Keys Only
    print(i)

for i in student.keys():                        # Keys Only
    print(i)

for i in student.values():                      # Values Only
    print(i)

for i in student.items():                       # Key-Value pair returned as a tuple
    print(i)
print(type(i))