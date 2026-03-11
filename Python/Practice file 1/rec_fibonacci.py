# Recursive function
def rec_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(rec_fibonacci(n-1) + rec_fibonacci(n-2))
   
n_terms = int(input("Enter the no. of fibonacci terms to be printed :\n"))
   
# check if the number of terms is valid
if n_terms <= 0:
   print("Invalid input ! Please input a positive value")
else:
   print("Fibonacci series:")
   for i in range(n_terms):
       print(rec_fibonacci(i))