class BalanceCheckable:
    def check_balance(self): 
        pass

class Depositable:
    def __init__(self, amount):
        self.amount = amount

    def deposit_amount(self): 
        return f"Depositing amount: {self.amount}"

class RegularAccount(BalanceCheckable, Depositable):
    def check_balance(self):
        return "Checking balance in RegularAccount."

class ReadOnlyAccount(BalanceCheckable):
    def check_balance(self):
        return "Checking balance in ReadOnlyAccount."

print("---------- Part 2: ----------")
regular = RegularAccount(1000)
print(regular.deposit_amount())
print(regular.check_balance())

roa = ReadOnlyAccount()
try:
    roa.deposit_amount()
except AttributeError as e:
    print(f"\nError: {e}")
print(roa.check_balance())