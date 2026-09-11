physics = float(input("Enter physics mark: "))
chemistry = float(input("Enter chemistry mark: "))
maths = float(input("Enter maths mark: "))
english = float(input("Enter english mark: "))
computer = float(input("Enter computer mark: "))

total = physics + chemistry + maths + english + computer
percentage = (total/500)*100

print("The total marks is",total)
print("The percentage marks is",percentage)

if percentage>=90:
    print("Grade A!")
elif percentage>=80:
    print("Grade B!")
elif percentage>=70:
    print("Grade C!")
elif percentage>=60:
    print("Grade D!")
else:
    print("Failed!")