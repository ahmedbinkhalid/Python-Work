limit = 10  # Specify the limit for the Fibonacci series
first_num = 0
second_num = 1

print("Fibonacci Series:")

for i in range(limit):
    if i == 0:
        print(first_num)  # Print the first number
    elif i == 1:
        print(second_num)  # Print the second number
    else:
        next_num = first_num + second_num
        next_num = first_num + second_num
        print(next_num)  # Print the next Fibonacci number
        first_num, second_num = second_num, next_num

print("Fibonacci series generated successfully.")  # Message upon successful completion
