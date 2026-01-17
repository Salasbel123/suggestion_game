from datetime import datetime 
class Employee:
    auto_id = 1          # للـ id الداخلي
    auto_emp_id = 1      # لتوليد emp_id
    employees = [] # help us to save data of employees 

    # ======================
    # Constructor
    # ======================
    def __init__(self, data):
        # we have tow number of id 
        #one named id example 1, 2, 3
        self.id = Employee.auto_id
        Employee.auto_id += 1
        #another named emp_id example EMP1, EMP2, EMP3
        self.emp_id = f"EMP{Employee.auto_emp_id}"
        Employee.auto_emp_id += 1

        self.name = data["name"]
        self.joining_date = datetime.strptime(data["joining_date"],"%Y-%m-%d").date()
        self.salary = data["salary"]

    # ======================
    # DISPLAY
    # ======================
  
    def display(self):
        return f"{self.id} | {self.emp_id} | {self.name} | {self.joining_date} | {self.salary}"

    # ======================
    # CREATE (class)
    # ======================
    @classmethod
    def create(cls, data):
        # here i call Constructor method by use cls(data) then stored in emp then add it in employees list that is class variable 
        # employees help us to stored data in runtime
        emp = cls(data)
        cls.employees.append(emp)
        print(f" Employee created with Emp ID: {emp.emp_id}")

    # ======================
    # SAVE (object)
    # ======================
    def save(self):
       #i use call the employees list by mention class name Employee 
       # then i ensure that data of employee that entered by Constructor method is saved in employees list
        Employee.employees.append(self)
        print(f"Employee saved with Emp ID: {self.emp_id}")

        print("\nAll Employees:")
        self.display()

    # ======================
    # UPDATE
    # ======================

    @classmethod
    def update(cls, emp_id, data):
        try:
            # محاولة تحويل emp_id إلى رقم صحيح
            emp_id = int(emp_id)
        except ValueError:
            print(" Invalid Employee ID. It must be a number.")
            return

       # after get emp_id check is this number exist in employees list 
       #by make loop in employees list then check if emp_id exist

        for emp in cls.employees:
            if emp.id == emp_id:
                try:
            #after ensure that emp_id is exsit start update
            #by get key of data if key name then change the value if the value of name not empty
            # else the value will still like what was been
                 
                    if data.get("name"):
                        emp.name = data["name"]

                  
                    if data.get("joining_date"):
                        try:
                            emp.joining_date = datetime.strptime(
                                data["joining_date"], "%Y-%m-%d"
                            ).date()
                        except ValueError:
                            print(" Invalid date format. Use YYYY-MM-DD.")
                            return

                   
                    if data.get("salary") != "":
                        # try:
                            emp.salary = float(data["salary"])
                        # except ValueError:
                            # print(" Invalid salary. It must be a number.")
                            return

                    print("Employee updated")
                    return

                except Exception as e:
                    print(f" An error occurred: {e}")
                    return

      
        print("Employee not found")




    # ======================
    # DELETE
    # ======================
    @classmethod
    def delete(cls, emp_id):
       
        emp_id = int(emp_id) 
          #after ensure that emp_id is exsit start delete 
        for emp in cls.employees:
            if emp.id == emp_id:
                cls.employees.remove(emp)
                print(" Employee deleted")
                return
        print(" Employee not found")

    # ======================
    # LIST + SEARCH + SORT
    # ======================
    @classmethod
    def list_employees(cls):
        if not cls.employees:
            print("No employees found")
            return

        print("""
    1. Search
    2. Sort
    """)

        choice = input("Choose option: ")

        # ======================
        # SEARCH
        # ======================
        if choice == "1":
            # if choose 1 you will have to choose one of these chances search by  emp_id or name
            print("Search by:")
            print("1. emp_id")
            print("2. name")
            search_choice = input("Choose: ")
           #then if you choose 1 you have to enter number of id 
            search_value = input("Enter search value: ")
            #this list will store reslut of search
            result = []

            if search_choice == "1":  # emp_id

        # loop on employees list to check if value of emp_id exist 
        #then add the data of this id number in result list
                for emp in cls.employees:
                    if search_value in emp.emp_id:
                        result.append(emp)

            elif search_choice == "2":  # name
                for emp in cls.employees:
                    if search_value in emp.name:
                        result.append(emp)

            else:
                print("Invalid choice")
                return

            if not result:
                print("No employees found")
                return

            print("\n--- Search Result ---")
            for emp in result:
                print(emp.display())

        # ======================
        # SORT
        # ======================
        elif choice == "2":
            print("Sort by:")
            print("1. emp_id")
            print("2. name")
            print("3. joining_date")
            print("4. salary")
#if you at first time choose 2 so you will have to choose type of sort
            sort_choice = input("Choose: ")
#if choose 1 th
            if sort_choice == "1":
                #here sort function will make sort on employees list by check emp_id in this list
                # lambda here pass employees list as object 'e' then we get all emp_id from employees
                # from e.emp_id 
                cls.employees.sort(key=lambda e: e.emp_id)
            elif sort_choice == "2":
                cls.employees.sort(key=lambda e: e.name)
            elif sort_choice == "3":
                cls.employees.sort(key=lambda e: e.joining_date)
            elif sort_choice == "4":
                cls.employees.sort(key=lambda e: e.salary)
            else:
                print("Invalid choice")
                return

            print("\n--- Sorted Employees ---")
            for emp in cls.employees:
                print(emp.display())

        else:
            print("Invalid option")



  


# ======================
# MAIN PROGRAM
# ======================
if __name__ == "__main__":

    data1 = {
        "name": "Hely",
        "joining_date": "2019-1-5",
        "salary": 3000
    }

    data2 = {
        "name": "salsabel",
        "joining_date": "2020-6-5",
        "salary": 2000
    }

    emp1 = Employee(data1)
    emp2 = Employee(data2)

    emp1.save()
    emp2.save()

    while True:
        print("""
        1. Create Employee
        2. Save Employee
        3. Update Employee
        4. Delete Employee
        5. List Employees
        6. Exit
        """)

        choice = input("Choose: ")

        if choice == "1":
            data = {
                "name": input("Name: "),
                "joining_date": input("Joining date: "),
                "salary": float(input("Salary: "))
            }
            Employee.create(data)

        elif choice == "2":
            data = {
                "name": input("Name: "),
                "joining_date": input("Joining date: "),
                "salary": float(input("Salary: "))
            }
            emp = Employee(data)
            emp.save()

        elif choice == "3":
            emp_id = input("Enter Emp ID to update (e.g. 1): ")
            data = {
                "name": input("New name (you can leave it empty): "),
                "joining_date": input("New date (you can leave it empty): "),
                "salary": input("New salary (you can leave it empty): ")
            }
            try:
               if data["salary"]:
            
                data["salary"] = float(data["salary"])
            except ValueError:
                print(" Invalid salary. It must be a number.")
            Employee.update(emp_id, data)

        elif choice == "4":
            emp_id = input("Enter Emp ID to delete (e.g. 1): ")
            Employee.delete(emp_id)

        elif choice == "5":
            Employee.list_employees()

        elif choice == "6":
            print("Bye 👋")
            break

        else:
            print("❌ Invalid choice")

