class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday to {self.name}! They are now {self.age} years old.")

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


person1 = Person("Adarsh", 19)
person1.greet()
person1.celebrate_birthday()
person1.introduce()
