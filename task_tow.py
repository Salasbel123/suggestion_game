
from collections import defaultdict #I will use it for solve //Group employees by department and get total salaries
from datetime import datetime #● Get first and last employee joined
import re # ● Exceptions and Error Handling
employees={
 "emp1":{   
    "emp_id":103,
    "name":"Salsabel",
    "joining_date":"2026/1/12",
    "salary":50000,
    "department":"Back-end"
    },
 "emp2":{
    "emp_id":102,
    "name":"Adel",
    "joining_date":"2024/1/12",
    "salary":70000,
    "department":"Back-end"
   
   },
    "emp3":{
    "emp_id":101,
    "name":"Adem",
    "joining_date":"2022/1/12",
    "salary":50000,
    "department":"Front-end"
   
   }
    }



 
#  ● List all employees
def list_all(**kwargs):
     for outer_key, inner_dict in kwargs.items():
        print(f"{outer_key}:")
        for inner_key, value in inner_dict.items():
            print(f"  {inner_key}: {value}")


# list_all(**employees)






def search_employee_by_id(emp_id, **kwargs):
    try:
        if not isinstance(emp_id, int):
            raise TypeError("Employee ID must be an integer.")
        
        # Check if emp_id is within the range of 100 and 500
        if not (100 <= emp_id <= 500):
            raise ValueError("Employee ID must be between 100 and 500.")

        # Create a list of employee IDs using map
        emp_ids = list(map(lambda x: kwargs[x]['emp_id'], kwargs.keys()))
        
        if emp_id not in emp_ids:
            print("Employee not found!")
            return

        for outer_key, inner_dict in kwargs.items():
            if inner_dict['emp_id'] == emp_id:
                print(f"Found Employee: {outer_key}:")
                for inner_key, value in inner_dict.items():
                    print(f"  {inner_key}: {value}")
                return

    except (TypeError, KeyError, ValueError) as e:
        print(f"Error: {e}")

# Get user input for emp_id***+
# try:
#     user_input = input("Please enter the Employee ID: ")
#     emp_id = int(user_input)  # Convert input to integer
#     search_employee_by_id(emp_id, **employees)  # Call the search function
# except ValueError:
#     print("Invalid input! Please enter a valid integer for Employee ID.")


#  ● Create, update and delete employee
# create


def create_employee(employees):
    try:
        emp_id = input("Enter Employee ID: ")
        # Use regex to ensure emp_id is a number
        if not re.match(r'^\d+$', emp_id):
            raise ValueError("Employee ID must be a valid integer.")
        emp_id = int(emp_id)

#  ● Emp_id id unique so don’t allow to add employee with existing employee emp_id
        if any(inner_dict['emp_id'] == emp_id for inner_dict in employees.values()):
            print("Employee ID already exists! Please use a unique ID.")
            return
        
        name = input("Enter Employee Name: ")
        # Validate name
        if not re.match(r'^[A-Za-z\s]+$', name):
            raise ValueError("Employee Name must contain only letters and spaces.")

        joining_date = input("Enter Joining Date (YYYY/MM/DD): ")
        # Validate the date format using regex
        if not re.match(r'^\d{4}/\d{1,2}/\d{1,2}$', joining_date):
            raise ValueError("Joining Date must be in the format YYYY/MM/DD.")

        salary = input("Enter Salary: ")
        # Use regex to ensure salary is a number
        if not re.match(r'^\d+$', salary):
            raise ValueError("Salary must be a valid integer.")
        salary = int(salary)

        department = input("Enter Department: ")
        # Validate department name (optional, can be removed if not necessary)
        if not re.match(r'^[A-Za-z\s]+$', department):
            raise ValueError("Department Name must contain only letters and spaces.")

        # Assign the new employee data
        new_emp_key = f"emp{len(employees) + 1}"
        employees[new_emp_key] = {
            "emp_id": emp_id,
            "name": name,
            "joining_date": joining_date,
            "salary": salary,
            "department": department
        }

        print(f"Employee '{name}' created successfully!")
        list_all(**employees)

    except ValueError as e:
        print(f"Error: {e}")

# Example Usage
# create_employee(employees)


# create_employee(employees)

# delete


def delete_employee(emp_id, employees):
    # Use filter to find employees who match the emp_id
    keys_to_delete = list(filter(lambda key: employees[key]['emp_id'] == emp_id, employees.keys()))

    if keys_to_delete:
        for key in keys_to_delete:
            del employees[key]  # Delete the employee from the dictionary
            print(f"Employee with ID {emp_id} has been deleted.")
    else:
        print("Employee not found!")

def list_employees(employees):
    if employees:
        print("\nRemaining Employees:")
        for key, value in employees.items():
            print(f"{key}: {value['name']} (ID: {value['emp_id']}, Department: {value['department']})")
    else:
        print("No employees remaining.")







# update


def update_employee(employees):
    try:
        emp_id = int(input("Enter Employee ID to update: "))

        # Find the employee with the given emp_id
        for outer_key, inner_dict in employees.items():
            if inner_dict['emp_id'] == emp_id:
                print("Current details:")
                print(f"{outer_key}:")
                for inner_key, value in inner_dict.items():
                    print(f"  {inner_key}: {value}")

                # Prompt the user for new values or keep current ones
                name = input("Enter new name (press enter to keep current): ")
                if name and not re.match(r'^[A-Za-z\s]+$', name):
                    print("Invalid name format. Name must only contain letters and spaces.")
                    return

                joining_date = input("Enter new joining date (YYYY/MM/DD or press enter to keep current): ")
                if joining_date and not re.match(r'^\d{4}/\d{1,2}/\d{1,2}$', joining_date):
                    print("Invalid date format. Please use YYYY/MM/DD.")
                    return

                salary = input("Enter new salary (press enter to keep current): ")
                if salary:
                    if not re.match(r'^\d+$', salary):
                        print("Invalid salary input. Salary must be a valid integer.")
                        return
                    inner_dict['salary'] = int(salary)

                department = input("Enter new department (press enter to keep current): ")
                if department and not re.match(r'^[A-Za-z\s]+$', department):
                    print("Invalid department format. Department must only contain letters and spaces.")
                    return

                # Update fields if provided
                if name:
                    inner_dict['name'] = name
                if joining_date:
                    inner_dict['joining_date'] = joining_date
                if department:
                    inner_dict['department'] = department
                
                list_all(**employees)
                print(f"Employee with ID {emp_id} updated successfully!")
                return

        print("Employee not found!")

    except ValueError:
        print("Invalid input! Please enter a valid integer for Employee ID.")

# Example Usage
# update_employee(employees)


#  ● Searching by emp_id and name

def search_employee_bynameid(emp_id=None, name=None):
    found = False
    for outer_key, inner_dict in employees.items():
        if (emp_id is not None and inner_dict['emp_id'] == emp_id) and(name is not None and inner_dict['name'].lower() == name.lower()):
            print(f"Found Employee: {outer_key}:")
            for inner_key, value in inner_dict.items():
                print(f"  {inner_key}: {value}")
            found = True

    if not found:
        print("Employee not found!")

# Example Usage
# try:
#     # Search by emp_id
#     emp_id_input = input("Enter Employee ID to search (press enter to skip): ")
#     emp_id = int(emp_id_input) if emp_id_input else None

#     # Search by name
#     name_input = input("Enter Employee Name to search (press enter to skip): ")
#     name = name_input if name_input else None

#     search_employee_bynameid(emp_id, name)

# except ValueError:
#     print("Invalid input! Please enter a valid integer for Employee ID.")




#  ● Sorting
def sort_employees(**kwargs):
    sorted_employees = dict(sorted(employees.items(), key=lambda item: item[1]["emp_id"]))

# Display sorted employees
    for emp_key, emp_info in sorted_employees.items():
       print(f" {emp_info}")

# sort_employees(**employees)

#  ● Employees report, example
#  Emp ID, Name, Joining Date, Department, Salary
#  259, Ahmed, 1/1/2014, Back-end, 50000
#  260, Omer, 1/1/2017, Back-end, 60000

def generate_employee_report(employees):
    print("Emp ID, Name, Joining Date, Department, Salary")
    for emp_info in employees.values():
        print(f"{emp_info['emp_id']}, {emp_info['name']}, {emp_info['joining_date']}, {emp_info['department']}, {emp_info['salary']}")

# Example usage
# generate_employee_report(employees)




# Grouping_department_salary(**employees)
def Grouping_department_salary(**kwargs):
    department_salaries = defaultdict(int)

    for emp_info in employees.values():
        department_salaries[emp_info["department"]] += emp_info["salary"]

    # Display the results
    print("Department, Total Salaries")
    for dept, total_salary in department_salaries.items():
        print(f"{dept}, {total_salary}")



#  ● Get first and last employee joined
# Convert joining_date to datetime objects for sorting
def Get_first_last_joined():

        employees_list = [(emp_key, emp_info) for emp_key, emp_info in employees.items()]

        # Sort employees by joining date
        employees_sorted = sorted(employees_list, key=lambda x: datetime.strptime(x[1]["joining_date"], "%Y/%m/%d"))

        # Get the first and last employees
        first_employee = employees_sorted[0]
        last_employee = employees_sorted[-1]

        # Display results
        print("First Employee Joined:", first_employee[1]["name"], "on", first_employee[1]["joining_date"])
        print("Last Employee Joined:", last_employee[1]["name"], "on", last_employee[1]["joining_date"])



#  ● Get employee with low and high salary
def low_high_salary():

    low_salary_emp = min(employees.values(), key=lambda emp: emp["salary"])
    high_salary_emp = max(employees.values(), key=lambda emp: emp["salary"])
    high_salary_emp["salary"]
    print(f'the highest salary: {high_salary_emp["name"]} : {high_salary_emp["salary"]}')
    print(f'the lowest salary: {low_salary_emp["name"]} : {low_salary_emp["salary"]}')


if __name__ == "__main__":

      while True:
        print("\nMenu:")
        print("1: List all employees")
        print("2: Search for an employee by ID")
        print("3: create new employee")
        print("4: update employee")
        print("5: delete employee")
        print("6: search for employee by ID and name")
        print("7: sorted employee")
        print("8: generate report employee")
        print("9: get first and last employee")
        print("10: get grouping Salary of each department ")
        print("11: get highest and lowest Salary of each employee ")
        print("12: Exit")
        
        choice = input("Please select an option (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 or 12): ")
        
        if choice == '1':
            list_all(**employees)
            
        elif choice == '2':
            try:
                emp_id_input = input("Enter Employee ID to search: ")
                emp_id = int(emp_id_input)  # Convert to integer
                search_employee_by_id(emp_id, **employees)
            except ValueError:
                print("Invalid input! Please enter a valid integer for Employee ID.")
        elif choice == '3':
             create_employee(employees)
             
        elif choice == '4':     
             update_employee(employees)

        elif choice == '5':     
            try:
                user_input = input("Please enter the Employee ID to delete: ")
                emp_id = int(user_input)  # Convert input to integer
                delete_employee(emp_id, employees)  # Call the delete function
                list_employees(employees)  # List remaining employees
            except ValueError:
                print("Invalid input! Please enter a valid integer for Employee ID.")

        elif choice == '6':     
             try:
                # Search by emp_id
                emp_id_input = input("Enter Employee ID to search (press enter to skip): ")
                emp_id = int(emp_id_input) if emp_id_input else None

                # Search by name
                name_input = input("Enter Employee Name to search (press enter to skip): ")
                name = name_input if name_input else None

                search_employee_bynameid(emp_id, name)

             except ValueError:
                print("Invalid input! Please enter a valid integer for Employee ID.")

        elif choice == '7':     
             sort_employees(**employees)

        elif choice == '8':     
             generate_employee_report(employees)

        elif choice == '9':     
             Get_first_last_joined() 

        elif choice == '10':     
             Grouping_department_salary(**employees) 

        elif choice == '11':     
             low_high_salary()

        elif choice == '12':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")