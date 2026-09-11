def atm():
    correct_pin = 1234
    balance = 5000

    try:
        pin = int(input("Enter PIN Number: "))
        if pin != correct_pin:
            raise ValueError("Wrong PIN Entered")
        print("Login Successful! ")
        amount = int(input("Enter the amount to withdraw: "))
        if amount > balance:
            raise ValueError("Insufficient Balance! ")
        balance -= amount
        print("Withdrawal Successful! ")
        print("Balance :",balance)

    except Exception as e:
        print("Error!!! ",e)

    finally:
        print("Thank you for Visiting us!")

atm()

