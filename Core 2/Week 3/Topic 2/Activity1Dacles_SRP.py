class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class PayrollCalculator(Employee):
    def calculate_payroll(self):
        return self.salary * 0.85
    
class EmployeeFileManager(Employee):
    def save_to_file(self):
        with open(f"{self.name}.txt", "w") as file:
            file.write(f"Name: {self.name}\nSalary: {PayrollCalculator.calculate_payroll(self)}")

class NotificationService(Employee):
    def send_email(self):
        print(f"Sending email to {self.name}......")

employee = Employee("Jessie", 500001)
payroll_calculator = PayrollCalculator(employee.name, employee.salary)
employee_file_manager = EmployeeFileManager(employee.name, employee.salary)
notification_service = NotificationService(employee.name, employee.salary)

print("Payroll:",payroll_calculator.calculate_payroll())
employee_file_manager.save_to_file()
notification_service.send_email()