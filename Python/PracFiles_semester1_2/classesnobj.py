class cat:

    #A simple class
    # attributes:-

    attr1= "cat"
    attr2= "meow"

    #a sample func
    def fun(self): #Tells u the object of the class like this in c++
        print("I am a ", self.attr1)
        print("and i ", self.attr2)


#Driver code
#Object instantiation

H = cat() #H is an object here.... object = classname()

#Accessing class attributes and methods through objects

print(H.attr1)
H.fun() #Function calling