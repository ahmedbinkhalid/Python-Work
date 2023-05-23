# Declaring a Tuple
clothes_tuple = ('pants', 'shirt', 'hat', 'socks')
print("The type of collection is: " + str(type(clothes_tuple)) + " and the collection is: " + str(clothes_tuple))
# changing the cell value
# declaring a list
clothes_list = list(clothes_tuple)
print("The type of collection is: " + str(type(clothes_list)) + ' and the collection is: ' + str(clothes_list))
# Changing value of a cell in list
clothes_list[0] = 'Trousers'
print(clothes_list)

# casting back the List as Tuple
clothes_tuple = tuple(clothes_list)
print("the type of collection is: " + str(type(clothes_tuple)) + " and the tuple is: " + str(clothes_tuple))

# Creating Tuple with 1 item
single_tuple = ('Ahmed',)
print(type(single_tuple))
print(single_tuple)
