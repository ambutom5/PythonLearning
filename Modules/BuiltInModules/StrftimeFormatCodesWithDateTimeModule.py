import datetime

x = datetime.datetime.now()

print(x.strftime("%d/%m/%Y"))
print(x.strftime("%m-%d-%Y"))
print(x.strftime("%B %d, %Y"))
print(x.strftime("%Y %B %d"))
print(x.strftime("%Y %b %d, %I.%M %p"))
print(x.strftime("%Y %b %y, %H.%M"))
print(x.strftime("%A, %d-%B-%Y"))
print(x.strftime("%d %B %Y | %I.%M %p "))
print(x.strftime("%Y/%m/%d %I.%M %p"))
print("Today is",x.strftime("%A,"),"the",x.strftime("%d"),"nd of",x.strftime("%B %Y"))
