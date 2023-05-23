# Nested Dictionary of Building Attendants
building_attendants = {'floor_1': {'first_apartment': 'Rachel', 'second_apartment': 'Jean'}, 'floor_2': {'third_apartment': 'Jack'}}

# printing nested cell of items of 1st floor
print(building_attendants['floor_1'])

# printing resident of 2nd apartment
print(building_attendants['floor_1']['second_apartment'])

# Adding 2nd resident to second floor

building_attendants['floor_2']['fourth_apartment'] = 'Carroll'
print(building_attendants)

# Deleting 1st apartment from the dictionary
building_attendants['floor_1'].pop('first_apartment') # 1st Way
# del building_attendants['floor_1']['first_apartment'] # 2nd Way
print(building_attendants)
