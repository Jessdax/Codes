 # Global Variable
menu = {"Pizza":{"Price" : 200,"Stock" : 5}, "Ice Cream":{"Price" : 50, "Stock" : 10 }} 
orders = []
def manage_menu():
# Local Variables
    while True:
        print("\n Restaurant Menu")
        print("----------------------------")
        print("Current Orders", orders)
        print("1. Add Foods")
        print("2. Edit Foods")
        print("3. Delete Food ")
# Input Validation for Menu Choices
        while True:
            try:
                choice = int(input("Enter Your Choice (1-3): "))
                if 1 <= choice <= 3:
                    break
                else:
                    print("Please Enter A Number Between 1 and 3: ")
            except ValueError:
                    print("Please Enter A Valid Number: ")
# Conditional handle each choice with repeat options
        if choice == 1: # Add Food
            while True:
                print("\nADD FOOD")
                print("-------------------------")
                food = str(input("Add New Food: "))
                if food in menu:
                    print("Food Already in the Menu. Enter New Food\n")
                else:
# Validate Price Input
                    while True:
                        try:
                            price = float(input("Price: P"))
                            if price < 0:
                                print("Price Cannot Be Negative. Please Enter A Positive Number: ")
                            else:
                                break
                        except ValueError:
                            print("Please Enter A Valid Number for Price: ")
# Enter A Valid Number for Stock
                    while True:
                        try:
                            stock = int(input("Stock Amount: "))
                            print("-------------------------")
                            if stock < 0 :
                                print("Price Cannot Be Negative. Please Enter A Positive Number: ")
                            else:
                                break
                        except ValueError:
                            print("Please Enter A Valid Number for Price: ")
                
                    menu[food] = {"price": price, "stock": stock}
                    print(f"Added {food} for P{price} with {stock} in stock\n")
                    print("UPDATED MENU")
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    print(menu)
                    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
                    again = input("Add Another Food?(y/n): ").lower()
                    if again != "y":
                            break
                    another = input("Do Another Action(y/n)?: ")
                    if another == "y":
                        manage_menu()
                    else:
                        break
            break
        if choice == 2: # Edit Food
            while True:
                print("EDIT FOOD")
                print("--------------------------------")
                food = str(input("Enter The Food You Wanted to Edit: "))
                if food not in menu:
                    print("Food not Found in the Menu. Please Enter A food in the menu")
                else:   
# Validate Price Input
                    while True:
                        try:
                            price = float(input("Enter New Price: P"))
                            if price < 0:
                                print("Price Cannot Be Negative. Please Enter A Positive Number: ")
                            else:
                                break
                        except ValueError:
                            print("Please Enter A Valid Number for Price: ")
# Enter A Valid Number for Stock
                    while True:
                        try:
                            stock = int(input("Enter Stock: "))
                            if stock < 0 :
                                print("Price Cannot Be Negative. Please Enter A Positive Number: ")
                            else:
                                break
                        except ValueError:
                            print("Please Enter A Valid Number for Price: ")
                            print("----------------------------------------------")
                    menu[food] = {"price": price, "stock": stock}
                    print("EDITED MENU")
                    print("*********************************************")
                    print(f"Edited {food} for P{price} with {stock} in stock")
                    print(menu)
                    print("*********************************************")
                    again = input("Add Another Food?(y/n): ").lower()
                    if again != "y":
                        another = input("Do Another Action(y/n)?")
                        if another == "y":
                            manage_menu()
                        elif another == "n":
                            break
            break
        if choice == 3: # Delete Food
            while True:
                food = str(input("Enter The Food You Wanted to Delete: "))
                if food  not in menu:
                    print("Food not Found in the Menu. Please Enter A food in the menu")
                else:
                    sure = input(f"Are you sure you want to delete {food}(y/n)?: ")
                    if sure != "n":
                        del menu[food]
                        print(f"The {food} is delete from the menu\n")
                        print("UPDATED MENU")
                        print("-------------------------")
                        print(menu)
                        print("-------------------------")
                    else:
                        manage_menu()

                    again = input("Delete Another Food?(y/n): ").lower()
                    if again != "y":
                        another = input("Do Another Action(y/n)?: ")
                        if another == "y":
                            manage_menu()
                        elif another == "n":
                            break
            break       
        break
manage_menu()

