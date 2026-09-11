from datetime import datetime

dob1 = "05-10-1990"
dob2 = "1990-10-05"

# Uses datetime.strptime to parse date of birth from a string.
# It is used to convert a string into a datetime.date object.

x = datetime.strptime(dob1,"%d-%m-%Y").date()
y = datetime.strptime(dob2,"%Y-%m-%d").date()

print(x)
# 1990-10-05
print(y)
# 1990-10-05











