# Task 1
Windows_serial_numbers = "abd-def-ghi-jkl"

# Task 2
new_serial1 = Windows_serial_numbers[0:3]
new_serial2 = Windows_serial_numbers[4:7]
new_serial3 = Windows_serial_numbers[8:11]
new_serial4 = Windows_serial_numbers[12:15]

# Task 3
new_serial1 = new_serial1.replace('abc', 'aaa')
new_serial2 = new_serial2.replace('def', 'bbb')
new_serial3 = new_serial3.replace('ghi', 'ccc')
new_serial4 = new_serial4.replace('jkl', 'ddd')

# Task 4
encoded_windows_serial_number = new_serial1 + "-" + new_serial2 + "-" + new_serial3 + "-" + new_serial4

# Task 5
print("This was the old serial number : " + Windows_serial_numbers + " and This is the encoded one: " + encoded_windows_serial_number)

