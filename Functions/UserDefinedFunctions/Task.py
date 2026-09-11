def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("A.Addition \nB.Subtraction \nC.Multiplication \nD.Division")

choice = input("Enter your choice: ")

if choice == 'A' or choice == 'a':
    print("Sum =",add(a,b))
elif choice == 'B' or choice == 'b':
    print("Difference =",sub(a,b))
elif choice == 'C' or choice == 'c':
    print("Multiplication =",mul(a,b))
elif choice == 'D' or choice == 'd':
    print("Division =",div(a,b))
else:
    print("Invalid")