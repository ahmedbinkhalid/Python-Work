# if statement practice assignment

# Task 1 -> creating employee dictionary
employee_dictionary = {'Jack': 6, 'Russel': 10, 'Karen': 2}
# print(employee_dictionary['Jack'])
# print(type(employee_dictionary['Jack']))
# Task 2 -> Checking who can work 5-8 hours

if employee_dictionary['Jack'] >= 5 and employee_dictionary['Jack'] <= 8:
    print('Jack can work between 5-8 hours')
elif employee_dictionary['Russel'] >= 5 and employee_dictionary['Russel'] <= 8:
    print('Russel can work between 5-8 hours')
elif employee_dictionary['Karen'] >= 5 and employee_dictionary['Karen'] <= 8:
    print("Karen can work Between 5-8 hours")
else:
    print("No one from employee dictionary can work between 5-8 hours")
# Task 3 -> Weekend work 2 or 4 hours
if employee_dictionary['Jack'] == 2 or employee_dictionary['Jack'] == 4:
    print("Jack is the Guy who can work")
elif employee_dictionary['Russel'] == 2 or employee_dictionary['Russel'] == 4:
    print('Russel is the Guy who can work')
elif employee_dictionary['Karen'] == 2 or employee_dictionary['Karen'] == 4:
    print("Karen is the one who can work")
    if employee_dictionary['Karen'] == 2:
        pass
    elif employee_dictionary['Karen'] == 4:
        pass
    else:
        print("Default exit point: Nested else")
else:
    print("No one from employee dictionary can work")
