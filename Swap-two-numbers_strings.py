
# Python code to swap two numbers/strings
# without using third variable
 
x = input("Value of x: ")
y = input("Value of y: ")
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# code to swap 'x' and 'y'
x, y = y, x
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)


#___________________________________________________________


# Python code to swap two numbers
# using + and - operators
 
x = int(input("Value of x: "))
y = int(input("Value of y: "))
 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
 
# Swap code
x = x + y
y = x - y 
x = x - y 
 
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
