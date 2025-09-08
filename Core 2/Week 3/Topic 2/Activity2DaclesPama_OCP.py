class Process_Payment:
    def __init__ (self, method, amount):
        self.method = method
        self.amount = amount
    
    def process(self):
        print(f"Processing Payment....")

class Credit_Card(Process_Payment):
    def process(self):
        print(f"Processing credit card payment of {self.amount}")

class Paypal(Process_Payment):
    def process(self):
        print(f"Processing PayPal payment of {self.amount}")

class Gcash(Process_Payment):
    def process(self):
        print(f"Processing Gcash payment of {self.amount}")

def get_payment_method(method: str, amount: float):
    payment_classes = {
        "credit card": Credit_Card,
        "paypal": Paypal,
        "gcash": Gcash
    }
    return payment_classes.get(method.lower(), Process_Payment)(method, amount)

class Send_Notification:
    def __init__(self, type, message):
        self.type = type
        self.message = message
    
    def process(self):
        print(f"Sending Notification....")

class Email(Send_Notification):
    def send(self):
        print(f"Sending Email: {self.message}")

class Sms(Send_Notification):
    def send(self):
        print(f"Sending SMS: {self.message}")

class Messenger(Send_Notification):
    def send(self):
        print(f"Sending Messenger: {self.message}")

def get_send_notification(type: str, message: str):
    notification_classes = {
        "email": Email,
        "sms": Sms,
        "messenger": Messenger
    }
    return notification_classes.get(type.lower(), Send_Notification)(type, message)

class Export_File:
    def __init__(self, format):
        self.format = format

    def export(self):
        print(f"Exporting Data to....")
    
class Pdf(Export_File):
    def export(self):
        print("Exporting data to PDF")

class Excel(Export_File):
    def export(self):
        print("Exporting data to Excel")

class Text(Export_File):
    def export(self):
        print("Exporting data to Word")

def get_export_file(format: str):
    export_classes = {
        "pdf": Pdf,
        "excel": Excel,
        "text": Text
    }
    return export_classes.get(format.lower(), Export_File)(format)

while True:
    print("Example 1:")
    method = input("Enter payment method (Credit Card/Paypal/Gcash): ")
    amount = float(input("Enter payment amount: "))
    payment = get_payment_method(method, amount)
    payment.process()
    print("----------------")

    print("Example 2:")
    type = input("Enter notification type (Email/SMS/Messenger): ")
    message = input("Enter notification message: ")
    notification = get_send_notification(type, message)
    notification.send()
    print("----------------")

    print("Example 3:")
    format = input("Enter export format (PDF/Excel/Text): ")
    export_file = get_export_file(format)
    export_file.export()
    print("----------------")

    again = input("Do you want to run the program again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Exiting the program....")
        break