#Developer Identification
DEVELOPER_NAME = "Adegoke Emmanuel"
DEVELOPER_MATRIC = "24/14421"
DEVELOPER_DEPARTMENT = "Computer Science"

balance = 5000

def check_balance():
    print("\nYour current balance is: ₦", balance)


def deposit_money():
    global balance
    amount = int(input("Enter amount to deposit: ₦"))

    if amount > 0:
        balance += amount
        print("Deposit successful.")
    else:
        print("Invalid amount.")


def withdraw_money():
    global balance
    amount = int(input("Enter amount to withdraw: ₦"))

    if amount > balance:
        print("Insufficient balance.")
    elif amount <= 0:
        print("Invalid amount.")
    else:
        balance -= amount
        print("Withdrawal successful.")


def atm_menu():
    while True:
        print("\nATM Simulation System")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit_money()
        elif choice == "3":
            withdraw_money()
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid option. Try again.")


atm_menu()