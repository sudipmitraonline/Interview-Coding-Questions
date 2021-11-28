
arr = list(map(int, input().split()))
print("Array is :",arr)
 
res = arr[::-1] #reversing using list slicing
print("Resultant new reversed array:",res)

# ______________________ OR ________________________

arr = list(map(int, input().split()))
print("Before reversal Array is :",arr)
 
arr.reverse() #reversing using reverse()
print("After reversing Array:",arr)

# ____________________ OR __________________________

import numpy as np
 
#The original NumPy array
new_arr=np.array([list(input().split())])
print("Original Array is :",new_arr)
 
#reversing using flip() Method
res_arr=np.flip(new_arr)
print("Resultant Reversed Array:",res_arr)

#____________________________________________________
