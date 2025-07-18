print("--------------- Activity A ---------------")
shopping_list = ["Milk", "Eggs", "Toothpaste", "Soap"]

# Write your code below:

# 1. Append 'Rice' and 'Banana'
shopping_list.append("Rice")
shopping_list.append("Banana")

# 2. Remove 'Soap'
shopping_list.remove("Soap")

# 3. Replace 'Toothpaste' with 'Toothbrush'
shopping_list[2] = "Toothbrush"

# 4. Pop the last item and store it in 'last_item'
last_item = shopping_list.pop()

# 5. Print last two items using slicing
print("Last 2 Items: ",shopping_list[2:])

# 6. Print the updated list and the popped item
print(f"Updated Shopping List: {shopping_list}")
print(f"Popped Item: {last_item}")

print("--------------- Activity B ---------------")
# Step 1
locked_items = ("Passport", "ID", "Cash")

# Step 2
# Try changing 'ID' and catch the error
try:
    locked_items[1] = "Driver's License"

except TypeError as e:
    print(f"Error Caught!: {e}")
# Step 3
# Create extras tuple
extras = ("Powerbank", "Map")

# Step 4
# Concatenate and store in final_pack
final_pack = locked_items + extras

# Step 5
# Print second item
print(f"2nd Item: {final_pack[1]}")

print("--------------- Activity C ---------------")
# Ask the user for the grocery list(tuple)
grocery_list = []

for i in range(5):
    grocery = input(f"Enter grocery: ")
    grocery_list.append(grocery)

# Allow the user to modify the list
remove_grocery = input("Remove grocery: ")
if remove_grocery in grocery_list:
    grocery_list.remove(remove_grocery)
    print(f"{grocery_list} has been removed.")
else:
    print(f"{remove_grocery} is not in the list.")

new_grocery = input("Add another grocery: ")
grocery_list.append(new_grocery)

popped_item = grocery_list.pop()

print(f"Final Grocery List: {grocery_list}")
print(f"Popped Grocery: {popped_item}")

# Ask user to create a travel bag(tuple)
bag = []
for i in range(3):
    item = input("What to put in travel bag: ")
    bag.append(item)

travel_bag = tuple(bag)

print(f"Travel Bag Includes: {travel_bag}")

# Ask the user to change the tuple
try:
    change_tuple = input("Do you want to replace an item in the travel bag(y/n): ")
    if change_tuple == "y":
        index_tuple = int(input("Enter the position of item to change: "))
        change = str(input("What to replace: "))
        travel_bag[index_tuple] = change
    else:
        print("OKI")
except TypeError as e:
    print(f"Error Caught!: {e}")

except ValueError as e:
    print(f"Caught Error!: {e}")
