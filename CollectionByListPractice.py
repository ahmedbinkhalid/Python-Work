# Task 1
list_of_cars = ["BMW", "Toyota", "Tesla", "Kia"]

# Task 2
print(list_of_cars[2])
# Printing By Negative Index
print(list_of_cars[-2])

# Task 3
equal_comparison = list_of_cars[1] == "Toyota"
print(equal_comparison)

# Task 4 (List of Mixed Values)
list_of_mixed_values = ["Jim", 3500, "Alex", 2.53, True]

# Task 5
print(list_of_mixed_values[1])
print(list_of_mixed_values[2])
# Another way of printing values between 0-3 (that is 1 and 2)
print(list_of_mixed_values[1:3])

# Task 6
# print(list_of_mixed_values[6])

# Task 7 (Adding Bonus Value in Task 1 list at last)
# list_of_cars.append('Alpha Romeo')
# print(list_of_cars)
# Another way to add at last
# list_of_cars.insert(4, 'Alpha Romeo')
# print(list_of_cars)

# we can also do it by adding 2 lists
extended_list = ['Alpha Romeo']
list_of_cars.extend(extended_list)
print(list_of_cars)


