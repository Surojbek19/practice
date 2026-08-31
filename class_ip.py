print("====== INHERITENCE ======")
# Parent > Child
# Parent class is the orignal/genaral class that provides attributes and methods
# Child class inherites parent behavior and can have itsown behavior
# If we mix "INHERITANCE"  and "ENCAPSULATION" then child can have direct access to parent's public and _protected states but not to __private one.
# But we can have access to __private state of parent through child.


class Animal:  # Parent class
    # state
    description = "This is a parent class for animals!"

    # constructure
    def __init__(self, voice):
        self.voice = voice

    # method

    def make_voice(self):
        print(f"The animal can make voice: {self.voice}!")


class Dog(Animal):  # Child class
    # state

    # constructure
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def action(self):
        print("I can protect you!!!")


class Cat(Animal):  # Child class
    # state

    # constructure
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def action(self):
        print("I can play with you!!!")


class Fish(Animal):  # Child class
    # state

    # constructure
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self.sound} - {self.sound}")

    def action(self):
        print("You can enjoy watching me swimming!!!")


dog = Dog("Rex", "Woof", True)
cat = Cat("Tom", "Meow", True)
fish = Fish("Nemo", "ZzzZ", False)

dog.introduce()
dog.action()
cat.introduce()
cat.action()
fish.introduce()


print("********")
# Srates from the parent
dog.make_voice()
fish.make_voice()

print("*********")
print(Animal.description)
print(Dog.description)

print(fish.voice, cat.voice, dog.voice)
