# Manipulation on List(Advanced)

# Declaring a List
numbers_list = [123, 111.9, 10000, 0.4]
print("The list is : " + str(numbers_list))

# Getting the list's length
print("Printing the length of the list : " + str(len(numbers_list)))

# Changing the value of a specific cell inside a list
numbers_list[1] = 10
print("Changing the value of index 1 and printing the list : " + (str(numbers_list)))

# Adding the value at the end of the list
numbers_list.append(15)
print("Printing the list after adding a value at the end : " + str(numbers_list))

# Adding an item at a specific cell in a list
numbers_list.insert(2, 1005)
print("Inserting an item in a list at cell 2 and printing it : " + str(numbers_list))

# Removing an item by mentioning the value
numbers_list.remove(1005)
print("The list after removing the value 1005 is : " + str(numbers_list))

# Removing an item by mentioning the cell index
# In first way, we can remove an item from last opposite to append()
numbers_list.pop()
print("Removing from last by using pop() : " + str(numbers_list))
# Removing by mention the cell index
numbers_list.pop(0)
print("After removing the item at cell index (0) is : " + str(numbers_list))
