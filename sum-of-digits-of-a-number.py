def SumofIntegers(n):
    
    sum = 0
    
    for digit in str(n): 
      sum = sum + int(digit)      
    return sum
   
n = int(input("Enter the number: "))
print(SumofIntegers(n))
