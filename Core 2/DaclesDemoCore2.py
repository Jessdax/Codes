# Interface: Base Student Info since students can only store students info
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

# Interface: Average computation 
class AverageCalculator:
    def compute_average(self, grades):
        total = sum(float(grade) for grade in grades)
        return total / len(grades)

# Interface: Remark generation
class RemarkGenerator:
    def get_remark(self, average):
        return "Passed" if average >= 75 else "Failed"

def student_checker(): # This code checks if the number of students is valid
    while True:
        try:
            no_students = input("Enter how many students: ").strip()
            # Check if input is empty before trying to convert
            if not no_students:
                print("Grade cannot be empty. Try again.")
                continue

            no_students = int(no_students)

            if no_students <= 0:
                print("Number of Students must not be negative. Try again.")
                continue

            return no_students

        except ValueError:
            print("Invalid input. Please enter a valid number.")

def grade_checker(i): # This code checks if the grade is valid
    while True:
        try:
            grade_input = input(f"Enter the grade {i + 1} (0-100): ").strip()

            # Check if input is empty before trying to convert
            if not grade_input:
                print("Grade cannot be empty. Try again.")
                continue

            grade = int(grade_input)

            if grade <= 0 or grade > 100:
                print("Grade must be between 1 and 100. Try again.")
                continue

            return grade

        except ValueError:
            print("Invalid input. Please enter a valid grade.")
            continue

def check_name(): # This code checks if the name is valid
    while True:
        try:
            name = input("Enter the name of the student: ").strip()
            if not name:
                print("Name cannot be empty. Try again.")
                continue

            if name.isdigit():
                print("Name cannot be a number. Try again.")
                continue

            if len(name) < 2:
                print("Name must be at least 2 characters long. Try again.")
                continue

            if not name[0].isalpha():
                print("Name must start with a letter. Try again.")
                continue

            return name
        
        except ValueError:
                print("Invalid Character. Try Again.")
                continue

# Main system class using composition
class GradingSystem:
    def __init__(self):
        self.students = []
        self.average_calculator = AverageCalculator()
        self.remark_generator = RemarkGenerator()

    def add_student(self): # Add students
        students_count = student_checker()
        for i in range(students_count):
            print(f"\nStudent {i + 1} Details")
            name = check_name()
            grades = [grade_checker(k) for k in range(3)]

            student = Student(name, grades)
            self.students.append(student)

            average = self.average_calculator.compute_average(grades)
            remark = self.remark_generator.get_remark(average)
            print(f"Average: {average:.2f}")
            print(f"Remark: {remark}")

    def display_summary(self): # Display class summary
        print("\nClass Summary:")
        for student in self.students:
            average = self.average_calculator.compute_average(student.grades)
            remark = self.remark_generator.get_remark(average)
            print(f"{student.name} - Average: {average:.2f}, Remark: {remark}")

# Main execution
grading_system = GradingSystem()
grading_system.add_student()
grading_system.display_summary()

# I chose ISP since the program is designed to handle specific tasks related to student grading, such as adding students, calculating averages, and generating remarks. Each class has a single responsibility, making the code modular and easier to maintain.