# Creating a Dictionary with nested entities
nested_Dictionary = {'dictA': {'key_1': 'value 1'}, 'dictB': {'key_2': 'value2'}}
print(nested_Dictionary['dictB']['key_2'])

# Joe Dictionary with inner layer
joe = {'Age': 35, 'Kids': {'David': 'Boy', 'Lisa': 'Girl'}}
print(joe['Kids'])
print(joe['Kids']['David'])

# Copying of an exact same dictionary
new_joe = joe.copy()
new_joe.pop('Kids')
new_joe['Kids'] = 2
print(new_joe)
new_joe.clear()
print(new_joe)
