from datetime import datetime

dob = "05-10-1990"
# dob should be a string in YYYY-MM-DD format
dtob = datetime.strptime(dob,"%d-%m-%Y").date()
today = datetime.now()
age = today.year - dtob.year
if (today.month,today.day) < (dtob.month,dtob.day):
    age -= 1
print(age)