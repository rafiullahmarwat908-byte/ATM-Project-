account_name = 'Rafiullah'
account_balance = 20000
atm_pin_code = 5678

pin_code = int(input("Enter Pin Code: "))

if pin_code == atm_pin_code:
    print("1. Balance Check \n2. Cash Withdraw \n3. Exit")
    option = int(input("Select Option: "))
    if option == 1:
        print("Account Balance: ", account_balance)
    elif option == 2:
        amount = int(input("Enter Amount to Withdraw: "))
        # Check amount
        if amount <= account_balance:
            account_balance -= amount
            print("Take your money\nThanks for using ATM")
        else:
            print("Insufficient Balance")
    elif option == 3:
        print("Please take your card.\nThanks for using ATM.")
    else:
        print("Please select valid option.")
else:
    print("Incorrect Pin Code")
    