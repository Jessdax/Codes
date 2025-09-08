class PaymentMethod:
    def pay(self, amount):
        pass

class Pay_by_credit(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₱{amount} via Credit Card.")

class Pay_by_cash(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₱{amount} via Cash on Delivery.")

class Pay_by_gcash(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₱{amount} via GCash.")

class Pay_by_paymaya(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ₱{amount} via PayMaya.")

class CODOnlyPayment(Pay_by_cash):
    def pay(self, amount):
        print(f"Paid ₱{amount} via COD (cash).")

class CreditOnlyPayment(Pay_by_gcash, Pay_by_paymaya, Pay_by_credit):
    def pay(self, amount):
        print(f"Paid ₱{amount} via Gcash.")

    def pay(self, amount):
        print(f"Paid ₱{amount} via PayMaya.")

    def pay(self, amount):
        print(f"Paid ₱{amount} via Credit Card.")

class Notification():
    def send(self, message):
        print(f"Notification: {message}")

class sendSMS(Notification):
    def send(self, message):
        print(f"SMS Notification: {message}")

class sendEmail(Notification):
    def send(self, message):
        print(f"Email Notification: {message}")

class Notifier():
    def send_notification(self, notifier: Notification, message: str):
        notifier.send(message)

def itemChecker():
    while True:
        item = str(input("Enter item name: ")).strip().capitalize()

        if item.isdigit():
            print("Item name cannot be a number. Please try again.")
            continue

        if item:
            return item
        
        else:
            print("Item name cannot be empty. Please try again.")

def quantityChecker():
    while True:
        try:
            quantity = int(input(f"Enter {item_name} quantity: ")) # Prompt user for item quantity
            if quantity <= 0:
                print("Quantity must be a positive integer. Please try again.")
                continue

            return quantity

        except ValueError:
            print("Invalid input or Empty. Please enter a numeric value for quantity.")
            continue

def priceChecker():
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

def amount_checker():
    while True:
        try:
            amount = int(input("Enter Amount paid by customer: "))
            if amount < 0 :
                print("Amount cannot be negative. Please enter a valid amount.")
                continue

            if amount < total_price:
                print("Amount paid is less than the total price. Please enter a valid amount.")
                continue

            if amount > total_price:
                print("Amount paid is over the total price. Try Again... ")
                continue

            return amount
        
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")
            continue

def edit_inputs(item, quantity, price):
    while True:
        choice = input("Do you want to edit anything? (item/quantity/price/none): ").lower()
        if choice == "item":
            item = itemChecker()
        elif choice == "quantity":
            quantity = quantityChecker()
        elif choice == "price":
            price = priceChecker()
        elif choice == "none":
            break
        else:
            print("Invalid choice.")

    print(f"Total price for {quantity} {item}(s): ₱{quantity * price}")
    return item, quantity, price

while True:
    print("----------Welcome to Online Grocery Ordering System----------")
    item_name = itemChecker()
    quantity = quantityChecker()
    unit_price = priceChecker()
    total_price = quantity * unit_price
    print(f"Total price for {quantity} {item_name}(s): ₱{total_price}")

    item_name, quantity, unit_price = edit_inputs(item_name, quantity, unit_price)

    print("---------- Payment Method ----------")
    method = input("Enter payment method (credit/cod): ")
    if method == "credit":
        type = input("Enter payment type (gcash/paymaya/credit): ").lower()
    else:
        print("Invalid Type. Try Again...")
        continue

    amount = amount_checker() 

    codpayment = CODOnlyPayment()
    creditpayment = CreditOnlyPayment()
    credit = Pay_by_credit()
    cash = Pay_by_cash()
    gcash_payment = Pay_by_gcash()
    paymaya_payment = Pay_by_paymaya()

    if method.capitalize() == "credit":
        if type == "gcash":
            gcash_payment.pay(amount)
        elif type == "paymaya":
            paymaya_payment.pay(amount)
        elif type == "credit":
            creditpayment.pay(amount)
        else:
            print("Invalid Type.")

    elif method == "cod":
        codpayment.pay(amount)

    print("---------- Notification ----------")
    message = input("How would you like the receipt to be sent? (sms/email): ").lower()

    notifier = Notifier()
    sms = sendSMS()
    email = sendEmail()

    if message == "sms":
        notifier.send_notification(sms, f"{total_price} is paid via {method } Payment processed successfully.")
    else:
        notifier.send_notification(email, f"{total_price} is paid via {method} Payment processed successfully.")

    print("---------- Summary ----------")
    print(f"Total Price: {total_price}\nItem(s): {item_name}\nPaid via {method}")
    if message == "sms":
        notifier.send_notification(sms, f"{total_price} is paid via {method } Payment processed successfully.")
    else:
        notifier.send_notification(email, f"{total_price} is paid via {method} Payment processed successfully.")
    print("-------------------------")

    again = input("Want to try again?(y/n):").lower()
    if again != "y":
        print("Thank you! Order Again...")
        break
    else:
        continue
