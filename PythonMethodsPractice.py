# Assignment Question 1
# creating a method and calling it 'sorting'
def sorting(*coding):
    #word = coding
    if 'java' in coding:
        for letter in 'java':
            print(letter)

    else:
        print("There is no 'java' in sorting method")
        print('\n')


sorting('python', 'java')
print('\n')
sorting('python', 'java', 'Go')
print('\n')
sorting('python', 'js', 'c++')

# Question 2
# Method for tax calculation

def tax_calculation(gross_salary, tax = 0.22):
    global salary
    salary = gross_salary * (1-tax)
    print(salary)
def salary_limit_tester(net_salary):
    if net_salary > 5800:
        print("The net_salary is above 5800 and value is: " + str(net_salary))
    else:
        print("The net_salary is below 5800 and value is: " + str(net_salary))
tax_calculation(5000, 0.2)
salary_limit_tester(salary)
tax_calculation(6000,0.22)
salary_limit_tester(salary)
tax_calculation(10000)
salary_limit_tester(salary)


