# Global Variable
inventory = {
    "Harry Potter": {"Author": "J.K Rowling", "Date of Publication": 1997, "Stock": 5},
}

def library():
    while True:
        print("\n BOOK INVENTORY")
        print("----------------------------")
        print("1. Add Book")
        print("2. Edit Book")
        print("3. Delete Book")
        print("4. Search Book")
        print("5. View All Books")
        
        while True:
            try:
                choice = int(input("Enter Your Choice (1-5): "))
                if 1 <= choice <= 6:
                    break
                else:
                    print("Please Enter A Number Between 1 and 5: ")
            except ValueError:
                print("Please Enter A Valid Number: ")

        if choice == 1:  # Add Book
            while True:
                print("\nADD BOOK")
                print("-------------------------")
                book = input("Add New Book: ")
                if book in inventory:
                    print("Book Already in the Library. Enter New Book\n")
                else:
                    author = input("Book Author: ")
                    date = int(input("Date of Publication (YEAR): "))
                    stock = int(input("Stock Amount: "))
                    inventory[book] = {"Author": author, "Date of Publication": date, "Stock": stock}
                    print(f"Added {book} by {author}, published in {date} with {stock} in stock\n")
                again = input("Add Another Book? (y/n): ").lower()
                if again != "y":
                    break
                another = input("Do Another Action(y/n)?: ")
                if another == "y":
                    library()
                else:
                    break
            break
        
        elif choice == 2:  # Edit Book
            book = input("Enter The Book You Want to Edit: ")
            if book not in inventory:
                print("Book not Found.")
            else:
                author = input("New Author: ")
                date = int(input("New Date of Publication (YEAR): "))
                stock = int(input("New Stock Amount: "))
                inventory[book] = {"Author": author, "Date of Publication": date, "Stock": stock}
                print(f"Updated {book}: {author}, {date}, {stock} copies\n")
            again = input("Edit Another Book? (y/n): ").lower()
            if again != "y":

                another = input("Do Another Action(y/n)?: ")
                if another == "y":
                    library()
                else:
                    break
            break
        elif choice == 3:  # Delete Book
            book = input("Enter The Book You Want to Delete: ")
            if book not in inventory:
                print("Book not Found.")
            else:
                del inventory[book]
                print(f"{book} has been deleted from the library.\n")
            again = input("Delete Another Book? (y/n): ").lower()
            if again != "y":
                break
            another = input("Do Another Action(y/n)?: ")
            if another == "y":
                library()
            else:
                break
            break
        
        elif choice == 4:  # Search Book
            print("\nSEARCH BOOK")
            print("-------------------------")
            search_type = input("Search By Author (AN) or Date of Publication (DOP)?: ").upper()
           
            if search_type == "AN":
                author = input("Enter the author name: ")
                found = False
                for book, details in inventory.items():
                    if details["Author"].lower() == author.lower():
                        print(f"{book}: {details}")
                        found = True
                if not found:
                    print("Author not found!")
            
            elif search_type == "DOP":
                date = int(input("Enter the year of publication: "))
                found = False
                for book, details in inventory.items():
                    if details["Date of Publication"] == date:
                        print(f"{book}: {details}")
                        found = True
                if not found:
                    print("No books found for this year!")
            else:
                print("Invalid choice!")
            again = input("Search Another Book? (y/n): ").lower()
            if again != "y":
                break
            another = input("Do Another Action(y/n)?: ")
            if another == "y":
                library()
            else:
                break
            break
   
        elif choice == 5:  # View All Books
            print("\nLIBRARY INVENTORY")
            print("----------------------------")
            for book, details in inventory.items():
                print(f"{book}: {details}")
            again = input(" Show Again? (y/n): ").lower()
            
            if again != "y":    
                    break    
            another = input("Do Another Action(y/n)?: ")
            if another == "y":
                library()
            else:
                break
        break
library()