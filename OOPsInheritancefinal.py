# Final Task for OOPs Inheritance
# First we create two classes one parent and other child

# Parent Class
class Employee:
    def __init__(self,years_of_experience, position_name, employee_name):
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.employee_name = employee_name

    def calculate_salary(self):
        based_salary = 2500
        calculated_salary = None
        if 0 > self.years_of_experience <=2:
            calculated_salary = based_salary + 1500
        elif 2 > self.years_of_experience <+5:
            calculated_salary = based_salary + 2500
        elif self.years_of_experience > 5:
            calculated_salary = based_salary + 3500
        else:
            print("Wrong input inserted about experience")
        print("The calculated salary is %s: " %calculated_salary)
        return calculated_salary

    def candidate_for_bonus(self, salary):
        salary_with_bonus = None

        if "front-end" in self.position_name:
            salary_with_bonus = salary * 1.1
        if self.years_of_experience > 2:
            salary_with_bonus = salary * 1.2
        print("The Bonus for employee in the position %s is %s: " %(self.position_name, salary_with_bonus))

#Child Class
class Programmer(Employee):
    def __init__(self, years_of_experience, position_name, employee_name):
        super().__init__(years_of_experience, position_name, employee_name)
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.employee_name = employee_name
    def print_data (self):
        print("The employee %s works in as a %s in 0ur company" %(self.employee_name, self.position_name))

junior_python_programmer = Programmer(1, "front_end", "Joseph")

# Executing the methods of python programmer
calculated_salary_junior_python_programmer = junior_python_programmer.calculate_salary()
junior_python_programmer.candidate_for_bonus(calculated_salary_junior_python_programmer)
junior_python_programmer.print_data()

print("\n")

senior_devops = Programmer(6, "senior_devops", "Dan")

calculated_salary_senior_devops = senior_devops.calculate_salary()
senior_devops.candidate_for_bonus(calculated_salary_senior_devops)
senior_devops.print_data()
