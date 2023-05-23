# Collection in Terms of Dictionary
dictionary_example = {"name": "Ahmed", 1: "Hassan", 'Number': 1}
print("This is a Dictionary Declaration Example : " + str(dictionary_example))

# Pullout of a value from a Dictionary Way 1
print(dictionary_example["name"])

# Pullout of a value from a Dictionary Way 2
print(dictionary_example.get("Number"))
print(dictionary_example.get(1))

# Removing a value using .pop()
dictionary_example.pop(1)
print("Removing a value using .pop() : " + str(dictionary_example))

# Print out all the 'keys' of the dictionary
print("Print out all the 'keys' of the dictionary : " + str(dictionary_example.keys()))

# Print out all the 'Values' of the dictionary
print("Print out all the 'Values' of the dictionary : " + str(dictionary_example.values()))

# Use a variable and place it inside a dictionary
new_value = "Hassan Javed"
new_dictionary = {'new': new_value}
print("New dictionary using a variable : " + str(new_dictionary))
