# Write a program to remove all duplicate characters from a string while
# preserving their first occurrence.

stringname = "Programming"
setname = set()
result = ""

for char in stringname:
    print(char)
    if char not in setname:
        result = result + char
        setname.add(char)

print("Original String is                      : ",stringname)
print("After Duplicate Removal the String is   : ",result)

