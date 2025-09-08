# Part 1
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def check_balance(self):
        print(f"{self.account_holder}'s balance is ₱{self.balance}")
        
    def deposit(self, amount):
        self.balance += amount
        print(f"₱{amount} deposited.")

print("---------- Part 1: ----------")
account1 = BankAccount("Jessie", 5000)
account1.deposit(3000)
account1.check_balance()
