# List Collection Task Advanced
# Task 1 -> Create a List of Employees
employee_list = ["Adam", "John", "Greg", "Danna", "Ashly"]

# Task 2 -> Printing the length of the List
print("The length of the Employee List is : " + str(len(employee_list)))

# Task 3 -> Remove John and add Jack instead at index 1
employee_list.remove("John")
employee_list.insert(1, "Jack")
print("After replacing Jack instead of John : " + str(employee_list))

# Task 4 -> Add Mavrik at index 3
employee_list.insert(3, "Mavrik")
print("After inserting Mavrik at 3 : " + str(employee_list))

# Task 5 -> Change Mavrik Position , first remove him
employee_list.remove("Mavrik")
employee_list.append("Mavrik")
print("Removing from 3 and adding Mavrik at the End :" + str(employee_list))

# Task 6 -> Remove Mavrik from the list
employee_list.pop(5)
print("After poping Mavrik : " + str(employee_list))

# Task Bonus -> Sort the list by 'abc'
employee_list.sort()
print("This is a sorted list by 'abc' : " + str(employee_list))
