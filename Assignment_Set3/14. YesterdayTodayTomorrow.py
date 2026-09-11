# 14. Write a Python program to print yesterday, today, tomorrow.

from datetime import date,timedelta

today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday  : ",yesterday)
print("Today      : ",today)
print("Tomorrow   : ",tomorrow)

print("Yesterday  : ",yesterday.strftime("%A %d, %B, %Y"))
print("Today      : ",today.strftime("%A %d, %B, %Y"))
print("Tomorrow   : ",tomorrow.strftime("%A %d, %B, %Y"))
