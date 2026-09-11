num = int(input("Enter the number: "))
oddeven = lambda num: "Even" if num % 2 == 0 else "Odd"
print(oddeven(num))