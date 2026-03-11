class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

    def eat(self, food):
        print(f"{self.name} is eating {food}.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")

my_dog = Dog("Daisy", "German Shepherd")
my_dog.bark()
my_dog.eat("dog food")
my_dog.sleep()
my_dog.display_info()
