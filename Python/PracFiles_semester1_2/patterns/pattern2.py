n = 5                          #no of rows
k = n * 2 - 2                  #no of spaces in the front 
for i in range(0, n):          #This block prints spaces 
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i+1):    #This block prints stars
        print("* ", end=" ")
    print("\r")
    
#        *  
#       *  *  
#      *  *  *  
#     *  *  *  *  
#    *  *  *  *  * 