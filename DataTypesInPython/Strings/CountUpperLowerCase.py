mystring = "Welcome to Luminar TechnoLabs"
upper = 0
lower = 0

for i in range(len(mystring)):
    if mystring[i].isupper():
        upper += 1
    elif mystring[i].islower():
        lower += 1

print("Count of uppercase is: ",upper)
print("Count of lowercase is: ",lower)