class GroceryItem:  # Declaring of Class Grocery Item
    def __init__(self, item_name, quantity, unit_price): # Declaring Parameters
        self.item_name = item_name
        self.quantity = quantity
        self.unit_price = unit_price
    
    def get_total_price(self): # Method to calculate total price
        return self.quantity * self.unit_price

    def display_info(self): # Method to display item information
            return f"\nItem: {self.item_name}\nQuantity: {self.quantity}\nPrice per item: P{self.unit_price}"

def check_item_name(): # Check if item name is empty or invalid
    while True:
        name = str(input("Enter item name: ")) # Prompt user for item name
        if name.isdigit():
            print("Please enter a valid item name.")
            continue
        
        if not name:
            print("Item name cannot be empty.")
            continue

        return name
    
def check_quantity():
    while True:
        try:
            quantity = int(input(f"Enter quantity: ")) # Prompt user for item quantity
            if quantity <= 0:
                print("Quantity must be a positive integer. Please try again.")
                continue

            return quantity

        except ValueError:
            print("Invalid input or Empty. Please enter a numeric value for quantity.")
            continue

def check_price():

    while True:
        try:
            price = float(input("Enter item price: P")) # Prompt user for item price
            if price < 0:
                print("Price cannot be negative. Please enter a whole number for price.")
                continue

            else:
                return price

        except ValueError:
            print("Invalid input or Empty. Please enter a whole number for price.")
            continue

grocery_list = [] # List to store grocery items
while True: 
    try: # Try block to handle exceptions
        number = int(input("How many Items: ")) # Ask the user for the number of items
    except ValueError:
        print("Please Enter a Valid Number.")
        continue # Exit the program if input is invalid

    for i in range(number): # Loop the user input
            print(f"\nEnter details for item {i + 1}:")
            item_name = check_item_name().capitalize()
            quantity = check_quantity()
            price = check_price()

            item = GroceryItem(item_name, quantity, price)  # Create an instance of GroceryItem
            grocery_list.append(item)   # Append the item to the grocery list
    
    break

# Display the summary
print("\n---------- Grocery Basket Summary ----------")
for item in grocery_list: 
    print(item.display_info()) # Call the display_info method to show item details
    print(f"Total price: P{item.get_total_price()}") # Call the get_total_price method to show total price

print("---------------------------------------------")

