# This is a Dictionary Basic Task

# Task 1 -> Dictionary of Alex
Alex = {'Age': 32, 'Married': "Yes", 'Kids': 3}

# Task 2 -> Extract all value and assign them variables
# Alex.pop('Age')
# Alex.pop('Married')
# Alex.pop('Kids')
Alex.clear()
print(Alex)
Age = int(32)
Married = str("Yes")
Kids = int(3)
Alex = {'AlexAge': Age, 'isMarried': Married, 'haveKids': Kids}
print(Alex)
update = {'AlexAge': 33, 'haveKids': 4}
Alex.update(update)
print(Alex)
print("The updated values of Dictionary are : " + str(Alex.values()))
print("The updated keys of Dictionary are : " + str(Alex.keys()))
