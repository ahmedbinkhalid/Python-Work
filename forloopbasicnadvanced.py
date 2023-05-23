# using for loop on a list to iterate and print elements
random_list = ['apple', 4, 5, 'banana', 'rabit', 'rabit']
for items in random_list:
    print(items)
print('\n')
# using for loop with if statement

for items in random_list:
    if items == 'rabit':
        print(items)
        break
print('\n')
# another example of it
item = 'Workout'
for char in item:
    if char == 'o':
        print(char)
        break
print('\n')
# using range -> 1st online only ending point
for x in range(4):
    print(x)
    if x == 2:
        break
print('\n')
# using start and end range to print
for w in range(8,14):
    print(w)
print('\n')
# using start, end, and increment value in range for loop
for s in range(5,50,15):
    print(s)
    if s == 20:
        break
print('\n')

# for loop advanced example

"""" Guideliness for bonues

1) I want you to build a formula for bonuses
2) Employees are placed in cells by their work ethic
3) give each employee a bonus which will be based on his place in the list, multiply it by 100 (bonus = place * 100)
4) The boss said to give bonus by jumping +3 each time in the list
5) The boss said the the first employee (cell index 0) does not deserve any bonus

"""
salary = [1500, 3000, 4000, 8000, 7000, 2400, 9000, 3500, 2300, 10000]

for place in range(0, 9, 3):
    salary_with_bonus = salary[place] + place * 100
    if place == 0:
        pass
    else:
        print(salary_with_bonus)
