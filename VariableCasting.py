# Variable Casting
print("Casting integers to string")

integer_variable = 5
integer_variable_casted_to_string = str(integer_variable)
print(integer_variable_casted_to_string)
print(type(integer_variable_casted_to_string))
print("******************")

print("Casting integers to float")
integer_variable_casted_to_float = float(integer_variable)
print(integer_variable_casted_to_float)
print(type(integer_variable_casted_to_float))
print("*******************")

print("Casting from float to integer")
float_variable_casted_to_integer = int(integer_variable_casted_to_float)
print(float_variable_casted_to_integer)
print(type(float_variable_casted_to_integer))
print("*******************")

print("Casting string to integer and float")
string_variable = "5"
string_variable_casted_to_integer = int(string_variable)
string_variable_casted_to_float = float(string_variable)
print(string_variable_casted_to_integer)
print(type(string_variable_casted_to_integer))
print(string_variable_casted_to_float)
print(type(string_variable_casted_to_float))
