import sqlite3
import random
import string

# Connect to HR database
conn = sqlite3.connect('hr.db')
cursor = conn.cursor()

# Ensure extra columns exist
cursor.execute("PRAGMA table_info(Employees)")
columns = [col[1] for col in cursor.fetchall()]

if "DepartmentName" not in columns:
    cursor.execute("ALTER TABLE Employees ADD COLUMN DepartmentName TEXT DEFAULT ''")

if "Salary" not in columns:
    cursor.execute("ALTER TABLE Employees ADD COLUMN Salary REAL DEFAULT 0.0")

# Create Employee table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees
(
    EmployeeID TEXT PRIMARY KEY,
    EmployeeName TEXT NOT NULL,
    DepartmentName TEXT DEFAULT '',
    Salary REAL DEFAULT 0.0
)
''')
conn.commit()

# Generate random unique Employee ID
def generate_employee_id():
    while True:
        new_id = "EMP" + ''.join(random.choices(string.digits, k=5))
        cursor.execute("SELECT 1 FROM Employees WHERE EmployeeID = ?", (new_id,))
        if not cursor.fetchone():  # ID is unique
            return new_id

# Create - Add a new employee
def create_employee():
    while True:
        employee_id = generate_employee_id()
        print(f"Employee ID: {employee_id}")

        employee_name = input("Enter Employee Name: ").strip()
        if not employee_name or employee_name.isdigit():
            print("Employee Name cannot be empty or just a number.")
            continue

        department_name = input("Enter Department Name: ").strip()
        if not department_name or department_name.isdigit():
            print("Department Name cannot be empty or just a number.")
            continue

        salary_input = input("Enter Salary (default 0.0): ").strip()
        if not salary_input:
            salary = 0.0
        else:
            try:
                salary = float(salary_input)
            except ValueError:
                print("Invalid salary input. Setting to 0.0.")
                salary = 0.0

        cursor.execute("""
            INSERT INTO Employees (EmployeeID, EmployeeName, DepartmentName, Salary)
            VALUES (?, ?, ?, ?)
        """, (employee_id, employee_name, department_name, salary))
        conn.commit()

        print(f"Employee {employee_name} added successfully with ID {employee_id}.")
        again = input("Do you want to add another employee? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Returning to main menu...")
            break

# Read - View all employees
def read_employees():
    cursor.execute("SELECT * FROM Employees")
    employees = cursor.fetchall()
    if employees:
        print("\n|--- Employee List ---|")
        for emp in employees:
            print(f"ID: {emp[0]} | Name: {emp[1]} | Dept Name: {emp[2]} | Salary: {emp[3]}")
    else:
        print("No employees found.")

# Update - Modify an employee's details
def update_employee():
    while True:
        employee_id = input("Enter Employee ID to update: ").strip()
        cursor.execute("SELECT 1 FROM Employees WHERE EmployeeID = ?", (employee_id,))
        if cursor.fetchone() is None:
            print("Employee ID not found.")
            return

        print("Leave a field blank if you don't want to change it.")
        new_name = input("Enter new Employee Name: ").strip()
        new_dept = input("Enter new Department Name: ").strip()
        new_salary = input("Enter new Salary: ").strip()

        updates = []
        params = []

        if new_name:
            if new_name.isdigit():
                print("Employee Name cannot be just a number.")
            else:
                updates.append("EmployeeName = ?")
                params.append(new_name)
        if new_dept:
            if new_dept.isdigit():
                print("Department Name cannot be just a number.")
            else:
                updates.append("DepartmentName = ?")
                params.append(new_dept)
        if new_salary:
            try:
                salary_val = float(new_salary)
                updates.append("Salary = ?")
                params.append(salary_val)
            except ValueError:
                print("Invalid salary. Skipping salary update.")

        if updates:
            params.append(employee_id)
            sql = f"UPDATE Employees SET {', '.join(updates)} WHERE EmployeeID = ?"
            cursor.execute(sql, params)
            conn.commit()
            print(f"Employee {employee_id} updated successfully.")
        else:
            print("No updates were made.")

        again = input("Do you want to update another employee? (yes/no): ").strip().lower()
        if again != 'yes':
            break

# Delete - Remove an employee
def delete_employee():
    while True:
        employee_id = input("Enter Employee ID to delete: ").strip()
        cursor.execute("SELECT 1 FROM Employees WHERE EmployeeID = ?", (employee_id,))
        if cursor.fetchone() is None:
            print("Employee ID not found.")
            return

        cursor.execute("DELETE FROM Employees WHERE EmployeeID = ?", (employee_id,))
        conn.commit()
        print(f"Employee {employee_id} deleted successfully.")

        again = input("Do you want to delete another employee? (yes/no): ").strip().lower()
        if again != 'yes':
            break

# Search employees by department
def search_by_department():
    while True:
        department_name = input("Enter Department Name to search: ").strip()
        if not department_name:
            print("Department Name cannot be empty.")
            continue

        cursor.execute("SELECT * FROM Employees WHERE DepartmentName = ?", (department_name,))
        employees = cursor.fetchall()
        if employees:
            print("\n|--- Employees in Department ---|")
            for emp in employees:
                print(f"ID: {emp[0]} | Name: {emp[1]} | Dept Name: {emp[2]} | Salary: {emp[3]}")
            break
        else:
            print("No employees found in this department.")

        again = input("Do you want to search another department? (yes/no): ").strip().lower()
        if again != 'yes':
            break

def view_sorted_by_salary():
    cursor.execute("SELECT * FROM Employees ORDER BY Salary ASC")
    salary = cursor.fetchall()
    if salary:
        print("\n|--- Employees Sorted by Salary ---|")
        for emp in salary:
            print(f"ID: {emp[0]} | Employee Name: {emp[1]} | Department: {emp[2]} | Salary: {emp[3]}")
    else:
        print("No employees found.")

def view_above_15k_salary():
    cursor.execute("SELECT * FROM Employees WHERE Salary > 15000 ORDER BY Salary ASC")
    salary = cursor.fetchall()
    if salary:
        print("\n|--- Employees with Salary Above 15k ---|")
        for emp in salary:
            print(f"ID: {emp[0]} | Employee Name: {emp[1]} | Department: {emp[2]} | Salary: {emp[3]}")
    else:
        print("No employees found with salary above 15k.")

# Menu
def menu():
    while True:
        print("\n|--- HR Employee Database ---------------------|")
        print("|1. Add Employee                               |")
        print("|2. View Employees                             |")
        print("|3. Update Employee                            |")
        print("|4. Delete Employee                            |")
        print("|5. Search by Department                       |")
        print("|6. View Employees Sorted by Salary            |")
        print("|7. View Employees with Salary Above 15k       |")
        print("|8. Exit                                       |")
        print("|----------------------------------------------|")
        choice = input("|Enter choice (1-8): ").strip()

        match choice:
            case '1':
                create_employee()
            case '2':
                read_employees()
            case '3':
                update_employee()
            case '4':
                delete_employee()
            case '5':
                search_by_department()
            case '6':
                view_sorted_by_salary()
            case '7':
                view_above_15k_salary()
            case '8':
                print("Exiting HR system...")
                break
            case _:
                print("Invalid choice! Please enter 1-8.")

menu()
conn.close()
