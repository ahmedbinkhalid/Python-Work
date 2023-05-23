# if statement part two basics

age = 30
name = 'James'

# Example 1 -> if condition with 'and' logical operator
if age > 20 and name == 'James':
    print("Everything is fine and you are above 20")
else:
    print("Some information is wrong please check again")

# Example 2 -> if condition with 'or' logical operator
if age > 20 or name == 'james':
    print("Everything is fine and you are above 20")
else:
    print("Some information is wrong please check again")

# Example 3 -> Nested 'if' statement
married = True
if age > 20 and name == 'James':
    if married == True:
        print("Allah bless you and your family")
    else:
        print("Nested 'else'")
else:
    print("Main 'else'")

# Example 4 -> Pass in if statement
if name == 'James':
    pass
