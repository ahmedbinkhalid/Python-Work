# Declaration of while loop
number = 0
while number <= 10:
    print("The number is: " + str(number))
    number += 1
print("\n")
# While loop with if and break statement

num = 0
while num < 5:
    if num == 3:
        break
    print("The number before break is: " + str(num))
    num += 1
    print("\n")

# While loop with else statement

counter = 0
while counter < 4:
    print("The counter is less than 4 and value is: " + str(counter))
    counter +=1
else:
    counter = counter * 5
    print("The counter is not less than 4")
    print("The multiplied value is: " + str(counter))

