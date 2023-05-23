# declaring a class
class Employee:
    def __init__(self, name, salary, attendance):
        self.name = name
        self.salary = salary
        self.attendance = attendance
    def show_employee_details(self):
        print('The name of the emplyee is: ', self.name, ' and salary is: ', self.salary)
    def check_attendance(self):
        print('The employee named: ', self.name, ' is ' + str(self.attendance))

sara = Employee('sara', '40000', True)
sara.show_employee_details()
sara.check_attendance()
Ahmed = Employee('Ahmed', '1000000', False)
Ahmed.show_employee_details()
Ahmed.check_attendance()
