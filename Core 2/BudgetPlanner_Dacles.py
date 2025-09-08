class AllowancePlanner:
    def __init__(self, allowance):
        self.allowance = allowance

class Food(AllowancePlanner):
    def calculate(self):
        if self.allowance <= 99:
            return self.allowance * 0.70
        elif self.allowance <= 199:
            return self.allowance * 0.60
        else:
            return self.allowance * 0.50

class Transport(AllowancePlanner):
    def calculate(self):
        if self.allowance <= 99:
            return self.allowance * 0.20
        elif self.allowance <= 199:
            return self.allowance * 0.25
        else:
            return self.allowance * 0.30

class Savings(AllowancePlanner):
    def calculate(self):
        if self.allowance <= 99:
            return self.allowance * 0.10
        elif self.allowance <= 199:
            return self.allowance * 0.15
        else:
            return self.allowance * 0.20

class Advice(AllowancePlanner):
    def give_advice(self):
        if self.allowance <= 99:
            return "Try to save even a small amount daily!"
        elif self.allowance <= 199:
            return "Great! Stick to your budget plan."
        else:
            return "Nice! Save more or build your emergency fund."

class Summary:
    def __init__(self, allowance, food, transport, savings, advice):
        self.allowance = allowance
        self.food = food
        self.transport = transport
        self.savings = savings
        self.advice = advice

    def display_summary(self):
        print("\n----- Daily Budget Breakdown -----")
        print(f"Total Allowance: ₱{self.allowance:.2f}")
        print(f"Food:           ₱{self.food.calculate():.2f}")
        print(f"Transport:      ₱{self.transport.calculate():.2f}")
        print(f"Savings:        ₱{self.savings.calculate():.2f}")
        print(f"\nAdvice: {self.advice.give_advice()}")

def get_allowance():
    while True:
        try:
            allowance = float(input("Enter your daily allowance in ₱: "))
            if allowance < 0:
                print("Allowance cannot be negative. Try again.")
                continue
            return allowance
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

# Main Interface
allowance = get_allowance()
food = Food(allowance)
transport = Transport(allowance)
savings = Savings(allowance)
advice = Advice(allowance)
    
summary = Summary(allowance, food, transport, savings, advice)
summary.display_summary()

# I applied Single Responsibility Principle because each class I created has it own responsibility and all related to the class itself.
# I also applied SRP because I think it is the best suited SOLID principle for this program.

# 5 Functional Requirements
# 1. The user must be able to input their allowance
# 2. The user must be able to see the breakdown of their allowance
# 3. The program must be able to calculate the allowance
# 4. The program must be able to calculate the food, transport, and savings based on the allowance
# 5. The program must be able to give advice based on the allowance
