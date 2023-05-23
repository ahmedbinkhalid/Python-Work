# this is simple string code
short_name_variable = "hello ninja, coders"
print(short_name_variable)
print(short_name_variable)

# Print the first letter of a string variable
name = "Ahmed"
print(name[0])
# another way of printing the first letter of string variable
first_letter = "Pakistan Zindabad"[0]
print(first_letter)

# Mixed upper and lower case letter variables

mixed_variable_case = "THIS IS MY CoDiNG JOuRNey"
print(mixed_variable_case)

# printing the upper string as the lower case letters

print(mixed_variable_case.lower())

# printing the upper string as upper case letters

print(mixed_variable_case.upper())

# printing the length of the variable

print(len(mixed_variable_case))

# use a "+" in a print command

print(mixed_variable_case + " " + name)

# replace a part of a string

first_serial_number = "NOP3344"
print("The changed serial number is: " + first_serial_number.replace('3344' , '5566'))

# The serial variable value i still the same

print("orignal serial no : " + first_serial_number)

# Replace a part of a string twice

second_serail_number = "NOP3344NOP"
print("The cahnged second serial is : " + second_serail_number.replace('NOP' , 'PON' , 2)) # the number at the end represents how many times we want to change the string

# Taking a part of a variable according to the index range

range_of_indexes = second_serail_number[0:3]
print(range_of_indexes)

# Adding spaces between multiple variables in the print
first_word = "Thank"
second_word = "You"
Third_word = "Coders !"
print(first_word + " " + second_word + " " + Third_word)

