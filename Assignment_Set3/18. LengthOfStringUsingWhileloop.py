# 18. Find length of a string in python using while loop.

mystring = input("Enter the string: ")
count = i = length = 0

while True:
    for char in mystring:
        count += 1
    break
print("Length of String: ",count)

while i < len(mystring):
    length += 1
    i += 1
print("Length of String: ",length)
