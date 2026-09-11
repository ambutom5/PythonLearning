# 21.Write a program to count the number of uppercase and lowercase letters in a
# string.

mystring = "ProgRamminG"
upper = 0
lower = 0

for char in mystring:
    if char.islower():
        lower += 1
    elif char.isupper():
        upper += 1

print("No of upper cases: ",upper)
print("No of lower cases: ",lower)

