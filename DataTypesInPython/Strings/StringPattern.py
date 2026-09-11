mystring = "Python"

print(len(mystring))

for i in range(len(mystring)):
    for j in range(i+1):
        print(mystring[j],end=" ")
    print()