class ATMAccount:
    def __init__ (self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            return f"Depositing {self.__balance}..."
        else:
            print(f"Invalid Amount! Please Deposit Positive Number and Greater than 0 \nBalance: {self.__balance}")
            exit()

    def withdraw(self, amount):
        try:
            if amount <= self.__balance:
                if amount < 0:
                    print("Invalid Amount! Please Enter Positive Number")
                    exit()
                self.__balance -= amount
                return f"Withdrawing {amount}..."
            else :
                return f"Error! Insufficient Balance"
        except ValueError as e:
            return (e)
        
    def get_balance(self):
        return f"Your final balance is: {self.__balance}"

account = ATMAccount(0)
# print(account.deposit(1000))
# print(account.withdraw(500))

deposit = int(input("Enter amount to deposit: "))
print(account.deposit(deposit))
withdraw = int(input("Enter amount to withdraw: "))
print(account.withdraw(withdraw))

print("")
print("Your final balance is:",account._ATMAccount__balance)