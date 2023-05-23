# Task 1
gross_salary = 10000
health_insurance = 430.99
rent = 1200
food = 400.5
salary_tax = 20  # percentage
donation_to_poor = 10  # percentage out of net salary
# Net salary calculations

net_salary_without_tax = gross_salary - (health_insurance + rent + food)  # 7968.51
final_net_salary = net_salary_without_tax- ((salary_tax / 100) * net_salary_without_tax)
print("The final net salary is : " + str(final_net_salary))

# Task 3
donation = (donation_to_poor / 100) * final_net_salary
remaining_net_salary = final_net_salary - donation
print("The donation for the poor is : " + str(donation))
print("The remaining net salary is : " + str(remaining_net_salary))

# Task 4
round_salary = round(remaining_net_salary, 2)
print("The rounded salary is : " + str(round_salary))
