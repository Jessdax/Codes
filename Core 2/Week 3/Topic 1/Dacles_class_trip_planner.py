class TripBudgetPlanner:
    def __init__(self):
        self.budget = float(input("\nEnter your total trip budget: P"))
        self.transport_cost = float(input("Enter your transport cost: P"))
        self.food_cost = float(input("Enter your food cost: P"))
        self.activity_cost = float(input("Enter your activity cost: P"))

    def calculate_total_cost(self):
        self.total_cost = self.transport_cost + self.food_cost + self.activity_cost
        return self.total_cost

    def compare_budget(self):
        if self.total_cost < self.budget:
            print(f"\nYou are within your budget. You still have P{self.budget - self.total_cost:.2f} left. Enjoy your trip!")
        elif self.total_cost > self.budget:
            print(f"\nYou are over budget by P{abs(self.budget - self.total_cost):.2f}. Consider adjusting your plan.")
        else:
            print("\nYou spent your entire budget. Plan executed perfectly!")

    def display_summary(self):
        print(f"\nBudget: P{self.budget:.2f}")
        print(f"Transport Cost: P{self.transport_cost:.2f}")
        print(f"Food Cost: P{self.food_cost:.2f}")
        print(f"Activity Cost: P{self.activity_cost:.2f}")
        print(f"\nTotal Cost: P{self.total_cost:.2f}")

# Main program
while True:
    print("---------- Input Your Trip Budget Details ----------")
    trip = TripBudgetPlanner()
    trip.calculate_total_cost()

    print("\n---------- Trip Budget Summary----------")
    trip.display_summary()

    print("\n---------- Availability ----------")
    trip.compare_budget()
    print("\n----------------------------------")

    again = input("Do you want to plan another trip? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thank you for using the Trip Budget Planner!")
        break

