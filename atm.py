balance = 1000  # Starting balance
pin = "1234"    # Simple PIN for login

# Login
entered_pin = input("Enter your PIN: ")
if entered_pin != pin:
    print("Incorrect PIN. Access denied.")
    exit()

# Menu loop
while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        print(f"Your balance is: ${balance}")

    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"${amount} deposited. New balance: ${balance}")
        else:
            print("Enter a positive amount.")

    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"${amount} withdrawn. New balance: ${balance}")
        else:
            print("Invalid amount or insufficient balance.")

    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
