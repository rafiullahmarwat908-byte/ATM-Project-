````markdown
# Python ATM Machine Project

## Project Description

This is a simple text-based ATM Machine project created using Python.  
The program allows a user to enter a PIN code and access basic ATM services such as checking account balance, withdrawing cash, and exiting the system.

This project is beginner-friendly and helps in understanding the basic concepts of Python programming.

## Features

- PIN code verification
- 3 attempts for incorrect PIN
- Balance checking option
- Cash withdrawal option
- Updated balance after withdrawal
- Exit option
- Error handling for invalid input
- User-friendly menu system

## Technologies Used

- Python

## Concepts Used

- Variables
- If-else conditions
- While loop
- Try-except error handling
- User input
- Basic arithmetic operations
- Menu-based program structure

## How the Program Works

1. The program starts by showing a welcome message.
2. The user is asked to enter a PIN code.
3. If the PIN is correct, the ATM menu is displayed.
4. The user can choose from the following options:
   - Balance Check
   - Cash Withdraw
   - Exit
5. If the user enters the wrong PIN, the program gives limited attempts.
6. After 3 incorrect attempts, the card is blocked.
7. The program also handles invalid inputs such as letters instead of numbers.

## ATM Menu Options

### 1. Balance Check

This option shows the account holder name and current account balance.

### 2. Cash Withdraw

This option allows the user to withdraw money from the account.  
If the withdrawal amount is greater than the available balance, the program shows an insufficient balance message.

### 3. Exit

This option exits the ATM program and displays a thank you message.

## Code

```python
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
````

## How to Run This Project

1. Install Python on your computer.
2. Open VS Code, PyCharm, or any Python editor.
3. Create a file named:

```text
atm_machine.py
```

4. Copy and paste the code into the file.
5. Run the program using this command:

```bash
python atm_machine.py
```

## Sample Output

```text
Welcome to Python ATM Machine
Enter Pin Code: 5678

Welcome, Rafiullah!

===== ATM Menu =====
1. Balance Check
2. Cash Withdraw
3. Exit
Select Option: 1

Account Holder: Rafiullah
Account Balance: Rs. 20000
```

## Project Purpose

The purpose of this project is to practice basic Python programming concepts by creating a simple ATM system.
It is useful for beginners who want to improve their logic-building skills in Python.

## Author

Rafiullah

## Internship

This project can be used as a beginner-level Python programming..

```

```
