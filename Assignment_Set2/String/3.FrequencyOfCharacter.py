# 3. Write a program to find the frequency of each character in a string.

mystring = "banana"
frequency = {}

for char in mystring:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char in frequency:
    print(char,":",frequency[char])

