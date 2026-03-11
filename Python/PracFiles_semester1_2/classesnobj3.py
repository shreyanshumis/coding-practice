class Car:
    def __init__(self, name, model, year, price, colour):
        self.name = name
        self.model = model
        self.year = year
        self.price = price
        self.colour = colour

    def carss(self):
        print("============================")
        print("|| Name", self.name)
        print("|| Model",self.model)
        print("|| Year",self.year)
        print("|| Price",self.price)
        print("|| Colour",self.colour)
        print("============================")

n= int(input("How many cars do you have?"))
for i in range(n):
    name = input("Enter name: ")
    model = input("Enter model: ")
    year = int(input("Enter year: "))
    price = input("Enter price: ")
    colour = input("Enter colour: ")
    
    carobj = Car(name,model,year,price,colour)
    carobj.carss()