# SecureATM - PIN, menu, deposits and withdrawals
correct_pin = "1234"
balance = 5000
history = []

pin = input("Enter your 4-digit PIN: ")
if pin == correct_pin:
    while True:
        print("\n1. Balance  2. Deposit  3. Withdraw  4. History  5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            print("Balance:", balance)
        elif choice == "2":
            amount = float(input("Deposit amount: "))
            if amount > 0:
                balance += amount
                history.append("Deposited " + str(amount))
                print("Deposit successful")
            else:
                print("Enter a positive amount")
        elif choice == "3":
            amount = float(input("Withdrawal amount: "))
            if amount > 0 and amount <= balance:
                balance -= amount
                history.append("Withdrawn " + str(amount))
                print("Withdrawal successful")
            else:
                print("Invalid amount or insufficient balance")
        elif choice == "4":
            for item in history:
                print(item)
            if not history:
                print("No transactions yet")
        elif choice == "5":
            print("Thank you. Final balance:", balance)
            break
        else:
            print("Invalid menu choice")
else:
    print("Incorrect PIN. Access denied.")
