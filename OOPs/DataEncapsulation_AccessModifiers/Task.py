class BankAccount:
    def __init__(self):
        self.__accountno = 123456789
        self.__balance = 5000
    def deposit(self):
        depamt = int(input("Enter amount to be deposited: "))
        self.__balance += depamt
        print("Amount Deposited Successfully!")
    def withdraw(self):
        withdrawamt = int(input("Enter amount to be withdrawn: "))
        if withdrawamt <= self.__balance:
            self.__balance -= withdrawamt
            print("Amount Withdrawn Successfully!")
        else:
            print("Insufficient Balance!")
    def display_balance(self):
        print("Balance is: ",self.__balance)

obj1 = BankAccount()

while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Balance Enquiry")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj1.deposit()
    elif choice == 2:
        obj1.withdraw()
    elif choice == 3:
        obj1.display_balance()
    elif choice == 4:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")



# Create Bank Account Class
# Pvt Attributes
# __accnt no
# __ balance
#
# create methods:
# deposit()
# withdraw()
# display balance()
#
# Acess balance only thru methods