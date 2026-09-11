try:
    num1 = int(input("Enter a number: "))
    result = 200 / num1

except ValueError:
    print("Value Error! ")
except ZeroDivisionError:
    print("Division By Zero! ")

else:
    print("Result is: ",result)

finally:
    print("Division Success")
