# PROJECT 1
# Write a python program to replicate a Banking system. The following features are mandatory:
# 1.Account login
# 2. Amount Depositing
# 3. Amount Withdrawal


balance = 10000
while True:
    print("\nBanking System Menu:")
    print("1. Account Login")
    print("2. Exit")
    choice = input("Enter your choice : ")
    if choice == '1':
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        if account_number == '1234567890':
            account_holder_name = "Adith"
        else:
            account_holder_name = "Unknown"
        if account_number == '1234567890' and pin == '1234':
            print("Login successful! Welcome",account_holder_name,"!")
            while True:
                print("\nAccount Menu:")
                print("1. Account Deposit")
                print("2. Account Withdrawal")
                print("3. Logout")
                account_choice = input("Enter your choice : ")
                if account_choice == '1':
                    amount = float(input("Enter the amount to deposit: "))
                    balance += amount
                    print("Deposited",amount," successfully. Your new balance is", balance,".")
                elif account_choice == '2':
                    amount = float(input("Enter the amount to withdraw: "))
                    if amount <= balance:
                        balance -= amount
                        print("Withdrew", amount," successfully. Your new balance is",balance,".")
                    else:
                        print("Insufficient funds!")
                elif account_choice == '3':
                    print("Logged out successfully.")
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")
        else:
            print("Invalid account number or PIN. Please try again.")
    elif choice == '2':
        print("Thank you for using the Banking System. Have a good day!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
