def calculate_LCM(x,y):
    if x > y:
        greater = x
    else:
        greater = y

    while(True):
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1

    return lcm

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(calculate_LCM(num1,num2))