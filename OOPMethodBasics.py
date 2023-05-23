# Declaration of a Method(OOPs)

def my_method():
    print("My name is Ahmed Bin Khalid")
my_method()

def salary_calculation(salary,tax):
    employee_salary = salary * tax
    print("Salary after tax deduction is: " + str(employee_salary))

salary_calculation(float(input("Enter your salary: ")), 0.98)
