# List of Names
guest_name = ["Jessie", "Ryan", "Micheal", "Carlos"]

# Ask the User
print("=" * 35)
name = str(input("Enter your name: ")).strip().capitalize()

# Checks the user if on the list
if name in guest_name:
    age = int(input("Enter your age: ").strip())   
    print("=" * 35)
    if age >= 18: # Checks the age
        print(f"Welcome, {name}! You may enter.")
        print("=" * 35)
    elif age < 18:
        print(f"Sorry, {name}, you're too young to enter.")
        print("=" * 35)
# prints if the name is not on the list
else: 
    print("=" * 35)
    print(f"Sorry, {name} you're not on the list.")
    print("=" * 35) 

if name not in guest_name:
# Registering
    prompt = str(input("Do you want to register?(y/n): "))
    if prompt == "y":
        n_name = str(input("Enter your name: "))
        guest_name.append(n_name)
        print(f"New Member: {guest_name}")

# For the new member
        age = int(input("Enter your age: ").strip())   
        print("=" * 35)
        if age >= 18: # Checks the age
            print(f"Welcome, {name}! You may enter.")
            print("=" * 35)
        elif age < 18:
            print(f"Sorry, {name}, you're too young to enter.")
            print("=" * 35)
    
    else:
        print("Goodbye!")
        
