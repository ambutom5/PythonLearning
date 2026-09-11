# 11.Write a program to count the occurrence of a given element in a tuple without
# using the count() method.

mytuple = (3,1,2,3,1,2,3,3)
element = int(input("Enter the element: "))
freq = {}

for item in mytuple:
    if item not in freq:
        freq[item] = 1
    else:
        freq[item] += 1

print("Frequency of",element,"is",freq[element])
for key,value in freq.items():
    print(key,":",value)


