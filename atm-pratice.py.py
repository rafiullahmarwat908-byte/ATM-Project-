account_name = "Rafiullah"
account_balance = 20000
atm_pin_code = 5678

print("Welcome to Python ATM Machine")

attempts = 3

while attempts > 0:
    try:
        pin_code = int(input("Enter Pin Code: "))

        if pin_code == atm_pin_code:
            print(f"\nWelcome, {account_name}!")

            while True:
                print("\n===== ATM Menu =====")
                print("1. Balance Check")
                print("2. Cash Withdraw")
                print("3. Exit")

                try:
                    option = int(input("Select Option: "))

                    if option == 1:
                        print(f"\nAccount Holder: {account_name}")
                        print(f"Account Balance: Rs. {account_balance}")

                    elif option == 2:
                        amount = int(input("Enter Amount to Withdraw: "))

                        if amount <= 0:
                            print("Please enter a valid amount.")

                        elif amount > account_balance:
                            print("Insufficient Balance.")

                        else:
                            account_balance -= amount
                            print("\nPlease take your money.")
                            print(f"Withdrawn Amount: Rs. {amount}")
                            print(f"Remaining Balance: Rs. {account_balance}")
                            print("Thanks for using ATM.")

                    elif option == 3:
                        print("\nPlease take your card.")
                        print("Thanks for using ATM.")
                        break

                    else:
                        print("Please select a valid option.")

                except ValueError:
                    print("Invalid input. Please enter numbers only.")

            break

        else:
            attempts -= 1
            print(f"Incorrect Pin Code. Attempts left: {attempts}")

    except ValueError:
        attempts -= 1
        print(f"Invalid input. Please enter numbers only. Attempts left: {attempts}")

if attempts == 0:
    print("\nYour card has been blocked due to too many wrong attempts.")
