try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    print(num1/num2)

except Exception as e:
    print("Error! ",e)

finally:
    print("Division Success")