num_rows = 10
k = 0
for i in range(0, num_rows):
    for j in range(0, k):
        print(end=" ")
    k = k + 2
    for j in range(0, i-1):
        print("* ", end="")
    print()

#    * 
#      * * 
#        * * * 
#          * * * * 
#            * * * * * 
#              * * * * * * 
#                * * * * * * * 
#                  * * * * * * * * 
