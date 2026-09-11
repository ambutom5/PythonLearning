# 1. Write a program to count the number of vowels, consonants, digits, spaces,
# and special characters in a given string.

stringname = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowelcount = consonantcount = digitcount = spacecount = specialcharcount = 0

for char in stringname:
    if char.isalpha():
        if char in vowels:
            vowelcount += 1
        else:
            consonantcount += 1
    elif char.isdigit():
        digitcount += 1
    elif char.isspace():
        spacecount += 1
    else:
        specialcharcount += 1

print("No of vowels is: ",vowelcount)
print("No of consonants is: ",consonantcount)
print("No of digits is: ",digitcount)
print("No of space is: ",spacecount)
print("No of special characters is: ",specialcharcount)

