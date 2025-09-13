# EMPLOYEE-MANAGEMENT-SYSTEM.py

employees = []  # List to store employee dictionaries


def input_integer(prompt):
    """Utility function to safely take integer input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def input_float(prompt):
    """Utility function to safely take float input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def add_employee():
    print("\n--- Add New Employee ---")
    while True:
        emp_id = input_integer("Enter Employee ID: ")

        # Prevent duplicate IDs
        if any(emp['id'] == emp_id for emp in employees):
            print("Employee ID already exists. Please enter a different ID.")
        else:
            break

    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = input_float("Enter Salary: ")

    employee = {
        'id': emp_id,
        'name': name,
        'department': department,
        'salary': salary
    }
    employees.append(employee)
    print("Employee added successfully!")


def view_employees():
    print("\n--- View All Employees ---")
    if not employees:
        print("The employee database is empty.")
        return

    for emp in employees:
        print(f"ID: {emp['id']}, Name: {emp['name']}, "
              f"Department: {emp['department']}, Salary: {emp['salary']}")


def search_employee():
    print("\n--- Search Employee by ID ---")
    emp_id = input_integer("Enter Employee ID to search: ")

    for emp in employees:
        if emp['id'] == emp_id:
            print(f"Found: ID: {emp['id']}, Name: {emp['name']}, "
                  f"Department: {emp['department']}, Salary: {emp['salary']}")
            return

    print("Employee not found.")


def update_employee():
    print("\n--- Update Employee Details ---")
    emp_id = input_integer("Enter Employee ID to update: ")

    for emp in employees:
        if emp['id'] == emp_id:
            print("Leave blank to keep current value.")
            new_name = input(f"Enter new name ({emp['name']}): ")
            new_department = input(f"Enter new department ({emp['department']}): ")

            # Salary update with validation
            while True:
                new_salary = input(f"Enter new salary ({emp['salary']}): ")
                if new_salary.strip() == "":
                    new_salary = emp['salary']
                    break
                try:
                    new_salary = float(new_salary)
                    break
                except ValueError:
                    print("Invalid salary. Please enter a number.")

            emp['name'] = new_name if new_name.strip() else emp['name']
            emp['department'] = new_department if new_department.strip() else emp['department']
            emp['salary'] = new_salary

            print("Employee details updated successfully!")
            return

    print("Employee not found.")


def delete_employee():
    print("\n--- Delete Employee ---")
    emp_id = input_integer("Enter Employee ID to delete: ")

    for emp in employees:
        if emp['id'] == emp_id:
            employees.remove(emp)
            print("Employee deleted successfully!")
            return

    print("Employee not found.")


def menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Update Employee Details")
        print("5. Delete Employee")
        print("6. Exit")
        print("----------------------------------")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Goodbye! Exiting Employee Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()
