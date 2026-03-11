# Sample class with init method
class Person:

    #init method or constructor
    def __init__(self, name):
        self.name = name

    #function
    def say_hi(self):
        print("Hello, my name is",self.name)

p = Person('Shrey') #making object named p =>
p.say_hi() #function calling => object.function() || prints the statement

