class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        print(f"\nYour current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nYou have successfully deposited ${amount:.2f}.")
            self.check_balance()
        else:
            print("\nDeposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("\nInsufficient funds.")
        elif amount <= 0:
            print("\nWithdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"\nYou have successfully withdrawn ${amount:.2f}.")
            self.check_balance()

def display_menu():
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def main():
    atm = ATM(100)  # Initial balance is set to $100 for demonstration purposes

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            try:
                amount = float(input("\nEnter the amount to deposit: $"))
                atm.deposit(amount)
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
        elif choice == '3':
            try:
                amount = float(input("\nEnter the amount to withdraw: $"))
                atm.withdraw(amount)
            except ValueError:
                print("\nInvalid input. Please enter a valid number.")
        elif choice == '4':
            print("\nThank you for using the ATM. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

# Run the ATM program
main()
