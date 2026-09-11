# 15. Write a Python program to print the next 5 days starting today.
from datetime import date,timedelta
today = date.today()

for i in range(0,5):
    print(today + timedelta(days=i))
print()
for i in range(0,5):
    print((today + timedelta(days=i)).strftime("%A: %d, %B, %Y"))

