# Initialize snack list and prices tuple
snacks = ["chips", "candy", "soda"]
prices = (1.50, 0.75, 1.25)

# Ask user how many snacks they want to add
num_new_snacks = int(input("How many snacks would you like to add? "))
new_prices = [price + 2.00 for price in prices]  # Add 2.00 to each original price

# Add new snacks to the list
for _ in range(num_new_snacks):
    new_snack = input("Enter the name of the new snack: ")
    new_price = float(input(f"Enter the price for {new_snack}: ")) + 2.00  # Add 2.00 to user-entered price
    snacks.append(new_snack)
    new_prices.append(new_price)

# Print updated snack list before removal
print(f"Snack list after addition: {snacks}")
print(f"Updated prices after addition: {new_prices}")

# Ask user for a snack to remove
snack_to_remove = input("Enter the name of the snack to remove: ")
found = False
for i in range(len(snacks)):
    if snacks[i].lower() == snack_to_remove.lower():
        snacks.pop(i)
        new_prices.pop(i)
        found = True
        break
if not found:
    print("Snack not found in the list.")

# Create a new tuple with an added price for a bonus snack
updated_prices = tuple(new_prices) + (2.00,)

# Display results
print("Just Kidding – this activity is a prank")
print(f"Updated snack list: {snacks}")
print(f"Snack count: {len(snacks)}")
print(f"Updated prices: {updated_prices}")
