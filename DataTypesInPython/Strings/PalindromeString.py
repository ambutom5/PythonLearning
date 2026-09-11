mystring = input("Enter a word: ")

# if mystring[0:] == mystring[::-1]:
#     print("Palindrome")
# else:
#     print("Not palindrome")
#
# OR

if mystring[:] == mystring[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")