# Advanced While Loops Practice

# Part A
# creating list of ages
ages_list = [5, 6, 24, 32, 21, 70]

# Look for the ages under 30 with While Loop
counter = 0
while ages_list[counter] < 30:
    print("The age is: " + str(ages_list[counter]))
    counter += 1
print("This is the value that stopped loop: " + str(ages_list[counter]))
print("\n")

# Part B
counter = 0
while ages_list[counter] < 30:
    if ages_list[counter] > 20:
        break
    print("The age is: " + str(ages_list[counter]))
    counter += 1
print("This is the value that stopped loop: " + str(ages_list[counter]))
print("\n")

# Part C
counter = 0
while ages_list[counter] < 70:
    print("The age is: " + str(ages_list[counter]+2))
    counter += 1
else:
    print("I'm inside else because of the cell: " +str(ages_list[counter]))
