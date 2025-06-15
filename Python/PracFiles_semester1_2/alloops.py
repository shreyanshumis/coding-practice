class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    def display_info(self):
        print(f"I am {self.name}.")


class Dog(Animal):
    def speak(self):
        return "Woof Woof"

class Cat(Animal):
    def speak(self):
        return "Meowwww"

def make_sound(animal):
    print(animal.speak())

dog = Dog("Daisy")
cat = Cat("Sally")

make_sound(dog)  # Output: Woof Woof
make_sound(cat)  # Output: Meowwwww

dog.display_info()  # Output: I am Daisy
cat.display_info()  # Output: I am Sally
