class ATM:
    def __init__(self):
        self.account_number = 0
        self.account_holder_name = ""
        self.balance = 0
    def create_account(self):
        self.account_number = int(input("Enter account number: "))
        self.account_holder_name = input("Enter account holder name: ")
        self.balance = int(input("Enter account balance: "))
        print("Account Created Successfully!")
    def deposit(self):
        deposit = float(input("Enter deposit amount: "))
        self.balance += deposit
        print("Amount Deposited Successfully!")
    def withdraw(self):
        withdraw = float(input("Enter withdraw amount: "))
        if withdraw <= self.balance:
            self.balance -= withdraw
            print("Amount Withdrawn Successfully!")
        else:
            print("Insufficient Balance!")
    def balance_enquiry(self):
        print("Account Balance:", self.balance)
    def mini_statement(self):
        print("-------------- Mini Statement --------------")
        print("Account Number:",self.account_number)
        print("Account Holder Name:", self.account_holder_name)
        print("Account Balance:", self.balance)

obj1 = ATM()

while True:

    print("1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Balance Enquiry")
    print("5.Mini Statement")
    print("6.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        obj1.create_account()
    elif choice == 2:
        obj1.deposit()
    elif choice == 3:
        obj1.withdraw()
    elif choice == 4:
        obj1.balance_enquiry()
    elif choice == 5:
        obj1.mini_statement()
    elif choice == 6:
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")




