# Decide how to split the allowance
try:
    # Ask the user to enter their allowance
    allowance = float(input("Enter your daily allowance in ₱: "))
    if allowance < 0:
        print("You entered a negative number.")
    else:
        if allowance < 100:
            print("\nTier: Budget")    # For Budget
            food_percent = .70
            transport_percent = .20
            savings_percent = .10
            advice = "Try to save even a small amount daily!"

        elif allowance < 200:
            print("\nTier: Regular")   # For Regular
            food_percent = .60
            transport_percent = .25
            savings_percent = .15
            advice = "Great! Stick to your budget plan."

        else:
            print("\nTier: Generous")  # For Generous
            food_percent = .50
            transport_percent = .30
            savings_percent = .20
            advice = "Nice! Save more or build your emergency fund."

        # Calculate amounts
        food = allowance * food_percent
        transport = allowance * transport_percent
        savings = allowance * savings_percent

        # Show the breakdown
        print("\n--- Daily Budget Breakdown ---")
        print("Food       : ₱", round(food, 2))
        print("Transport  : ₱", round(transport, 2))
        print("Savings    : ₱", round(savings, 2))
        print("\nAdvice: " + advice)
        print("Total allowance checked: ₱", allowance)

except (ValueError):
            print("Error! Enter a number.")


