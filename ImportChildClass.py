#Child Class
from ImportParentClass import Employee


class Programmer(Employee):
    def __init__(self, years_of_experience, position_name, employee_name):
        super().__init__(years_of_experience, position_name, employee_name)
        self.years_of_experience = years_of_experience
        self.position_name = position_name
        self.employee_name = employee_name
    def print_data (self):
        print("The employee %s works in as a %s in 0ur company" %(self.employee_name, self.position_name))
