# Part 3
class BalanceCheckable:
    def check_balance(self):
        pass

class BankAccount(BalanceCheckable):
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

class ReadOnlyAccount(BalanceCheckable):
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

class BalanceService:
    def __init__(self, checker: BalanceCheckable):
        self.checker = checker
        
    def show(self):
        print(f"🧾 Account Balance: ₱{self.checker.check_balance()}")

print("---------- Part 3: ----------")
# Test with BankAccount
bank_account = BankAccount(1000)
bank_service = BalanceService(bank_account)
bank_service.show()

# Test with ReadOnlyAccount
readonly_account = ReadOnlyAccount(500)
readonly_service = BalanceService(readonly_account)
readonly_service.show()