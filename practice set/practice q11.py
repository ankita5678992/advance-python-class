class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        print("Balance:", self.balance)


acc = BankAccount()

acc.deposit(1000)
acc.withdraw(200)
acc.check_balance()