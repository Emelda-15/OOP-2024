class Bank_Account:
    # Class variable (interest rate)
    interest_rate = 0.05

    # Constructor
    def __init__(self, account_owner):
        self.account_owner = account_owner
        self.balance = 0.0 

    # Method to deposit an amount
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Negative deposit.")

    # Method to withdraw an amount
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("This amount is insufficient.")

    # Method to apply interest based on class variable interest_rate
    def apply_interest(self):
        self.balance += self.balance * Bank_Account.interest_rate

    # Method to display account information
    def display_account_info(self):
        print(f"Account_owner: {self.account_owner}, Balance: {self.balance:.2f}")


# Creating two instances of BankAccount with different account holders
account1 = Bank_Account("Gavin")
account2 = Bank_Account("Sheba")

# Performing deposits and withdrawals
account1.deposit(2000)
account1.withdraw(300)
account1.apply_interest()

account2.deposit(400)
account2.withdraw(200)
account2.apply_interest()

# Displaying account information
account1.display_account_info()
account2.display_account_info()
