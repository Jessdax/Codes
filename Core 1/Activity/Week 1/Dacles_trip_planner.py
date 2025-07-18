# Budget Planner Prompt
# Loop the prompt
number = int(input("How many plan you have?: "))
for i in range(number):
    print("*" * 40)
    print("         Budget Planner")
    print("*" * 40)
    t_budget = int(input("  How much is your budget?: P"))
    transport_cost = int(input("   How much for transport?: P"))
    food_cost = int(input("     How much for foods?: P"))
    activity_cost = int(input("   How much for activities?: P"))
    total_cost = transport_cost + food_cost + activity_cost
    budget_left = t_budget - total_cost
    print("*" * 40)

# Output
    print(f"          Budget: P{t_budget}")
    print(f"        Total Cost: {total_cost}" )

#Checking of total cost if fitted to the total budget
    print("*" * 60)

    print("----------Availability----------")
if total_cost < t_budget:
    print(f"You are within your budget. You still have P{budget_left} left. Enjoy your trip.")

elif total_cost > t_budget:
# Converting positive and negative numbers to absolute using ABS
    budget_left = abs(budget_left)  
    print(f"You are over budget by P{budget_left}, Consider adjusting your plan.")

else:
    print(f"You spent your entire budget. Plan Executed perfectly! ")

    print("*" * 60)
