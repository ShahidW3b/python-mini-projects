class BankAccount: 
    def __init__(self, owner_name, account_number, balance): 
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance

    def describe_account(self):
        print(
            f"Owner : {self.owner_name.title()}\n"
            f"Account Number : {self.account_number}\n"
            f"Balance : {self.balance}"
        )

    def show_balance(self):
        print(f"\nCurrent Balance : ${self.balance}")

    def deposit(self, amount): 
        if amount > 0: 
            self.balance += amount
            print(f"${amount:.2f} depostied succssfully.")
            self.show_balance()
        else: 
            print("Deposite amount must be grather than zero.")


    def withdraw(self, amount): 
        if amount <= 0: 
            print("Withdrawal amount must be grather than zero.")
        elif amount > self.balance: 
            print("Insufficient balance.")
        
        else: 
            self.balance -= amount
            print(f"$ {amount:.2f} withdrawed successsfully.")
            self.show_balance()



account = BankAccount("shahid", 234767, 1250)


while True: 
    print("\n==== ATM MENU ====")
    print("1. Show account information")
    print("2. Check Balance")
    print("3. Deposite Money")
    print("4. Withdraw money")
    print("5. Exit")

    choice = input("Chose an option (1-5): ")

    if choice == "1": 
        account.describe_account()

    elif choice == "2": 
       account.show_balance()
        
    elif choice == "3": 
        try: 
            amount = float(input("Enter depoist amount: $"))
            account.deposit(amount)

        except ValueError: 
            print("Enter a valid number.")

    elif choice == "4": 
        try: 
            amount = float(input("Enter the withdraw amount: $"))
            account.withdraw(amount)

        except ValueError:
            print("Enter a valid number.")

    
    elif choice == "5": 
        print("Thanks for using the ATM.")
        break

    
    else: 
        print("Chose a valid option please 1-5.")



