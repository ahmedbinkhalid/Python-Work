# Passing Keyword Arguments into Python OOPs Method
def my_phone_company(brand1, brand2, brand3):
    print("My phone brand2 is: " + brand2)

my_phone_company(brand2="Poco", brand1="Oppo", brand3="Apple")

# Arbitrary Arguments (Positional Arguments)
def my_clothings_company(*clothing): # one * means getting values as a tuple
    print('the last company is: ' + clothing[-1])

my_clothings_company('H&M', 'J.', 'Zara')
my_clothings_company('Gucci', 'SpiceBomb')

# Arbitrary Arguments (Positional Arguments) as a dictionary
def my_clothings_company2(**clothing2): # Two ** means getting values as a Dictionary
    print('the last company is: ' + clothing2["Pants"])

my_clothings_company2(shirts='H&M',Pants= 'J.',Shoes= 'Zara')
my_clothings_company2(Bag ='Gucci', Pants ='SpiceBomb')
