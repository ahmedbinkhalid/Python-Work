# Creating a tuple with some items
technological_terms = ('python', 'pycharm IDE', 'tuple', 'collections', 'string')

# Task 2 -> printing according to the instructions
print("We are ninja developers. We write " + str(technological_terms[0]) + " code in " + str(technological_terms[-4]) + ", and now practicing " + str(technological_terms[2]) + " collections topic, that contains " + str(technological_terms[-1]) + " variables")

# Adding 'float' and 'list' into the tuple
# first we cast tuple into list
technological_terms_list = list(technological_terms)
technological_terms_list.insert(5, 'float')
technological_terms_list.append('list')
# casting the list back to tuple
technological_terms = tuple(technological_terms_list)
print("The datatype is: " + str(type(technological_terms)) + ' and the collection is: ' + str(technological_terms))

# Creating a tuple with just 1 item
one_item = (1,)
print(type(one_item))
print(one_item[0])
