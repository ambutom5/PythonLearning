str1 = input("Enter a string: ")
list1 = list(str1)
list2 = []

print(list1)

for i in range(len(list1)-1,-1,-1):
    list2.append(list1[i])
print(list2)

if list1 == list2:
     print("Palindrome")
else:
    print("Not Palindrome")