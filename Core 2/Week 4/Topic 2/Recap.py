# Scenario 1
# print("Scenario 1: StudentProfile Overload (SRP)")
class StudentProfile:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Calculate_GPA(StudentProfile):
    def calculate_gpa(self):
    # logic here
        pass

class SaveProfile(StudentProfile):
    def save_to_file(self):
    # file writing
        pass

class SendEmail(StudentProfile):
    def send_email(self):
        print("Sending email to student...")

# student= StudentProfile("Jessie", 90)

# calcu = Calculate_GPA(student.name, student.grade)
# calcu.calculate_gpa()

# save = SaveProfile(student.name, student.grade)
# save.save_to_file()

# send = SendEmail(student.name, student.grade)
# send.send_email()

# Scenario 2
# print("\nScenario 2: PaymentHandler if-else Spiral (OCP)")
class PaymentMethod:
    def process(self, method):
        self.method = method

class GCash(PaymentMethod):
    def process(self):
        print("Paying with GCash")

class Paypal(PaymentMethod):
    def process(self):
            print("Paying with PayPal")

# payment = PaymentMethod()

# methods = [GCash(), Paypal()]
# for method in methods:
#     method.process()

#Scenario 3
# print("\nThe Bird That Can't Fly (LSP)")
class FlyingBird:
    def fly(self):
        print("Flying...")

class FlightlessBird:
    def walk(self):
        print("Walking...")

class Parrot(FlyingBird):
    pass

class Penguin(FlightlessBird):
    pass

# fbird = FlyingBird()
# parrot = Parrot()
# parrot.fly()

# flbird = FlightlessBird()
# penguin = Penguin()
# penguin.walk()
