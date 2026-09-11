mystring = "Welcome to Luminar TechnoLabs"
upper = 0
lower = 0
other = 0

for i in mystring:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    else:
        other += 1

print("Count of uppercase is: ", upper)
print("Count of lowercase is: ", lower)
print("Count of other characters is: ", other)