class Employee:
    def __init__(self, code, name, department, designation, salary, address, phone_number):
        self.code = code
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = salary
        self.address = address
        self.phone_number = phone_number

employee1 = Employee("E001", "Shreyanshu", "HR", "Manager", 35000, "Navi Mumbai", "1234567890")
print("Employee Code:", employee1.code)
print("Employee Name:", employee1.name)
print("Department:", employee1.department)
print("Designation:", employee1.designation)
print("Salary:", employee1.salary)
print("Address:", employee1.address)
print("Phone Number:", employee1.phone_number)
