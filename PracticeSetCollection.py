# 'Set' collection of Drinks
drinks_set = {"Coia","Sprite", "Beer", "Water", "Soda"}

# Adding additional cell "Soda"
drinks_set.add("Soda")
print(drinks_set)

# Deleting a Soda out of the Cell
drinks_set.remove("Soda")
print(drinks_set)

# Making copy of the set
drinks_2 = drinks_set.copy()
print(drinks_2)

# Bonus -> Printing the length of the items inside a set
print(len(drinks_set))
