# 3. Write a Python program that prompts the user to input an integer and raises a
# ValueError exception if the input is not a valid integer.

try:
    n = int(input("Enter an integer: "))

except ValueError:
    print("Input is not a valid integer!")


