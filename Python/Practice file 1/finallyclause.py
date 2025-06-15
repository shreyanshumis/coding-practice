#The code given in finally executes irrespective of the presense of errors or not
def func1():
    try:
        l = [1,2,4,56]
        i= int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("An error occured")
        return 0

    #FINALLY CLAUSE - Always executes
    finally:
        print("I am always executed")

#If we just printed instead of finally, it wouldn't have executed.

x = func1()
print(x)