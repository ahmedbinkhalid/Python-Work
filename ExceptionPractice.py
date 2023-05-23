# Exception 1
try:
    x = 5
    print("The Number is: "+x)
except:
    print("The Number is: "+ str(x))

# Exception 2
try:
 x+5
 print("The value is: " + str(z))
except:
 print("If x is not defined give x the value and print it in z which is also not intialized")
 x=3
 z= x + 5
 print(z)

# Exception 3
try:
 list = [1,2,3,4]
 print(list[6])
except:
 print("If the out of index value is tried to be printed, print last index instead")
 print(list[-1])
