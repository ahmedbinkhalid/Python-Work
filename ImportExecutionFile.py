from ImportChildClass import Programmer

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
