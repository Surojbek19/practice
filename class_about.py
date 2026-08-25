print("==== What is class =====")
# class - blueprint for object creation
# structure - state > constructure > method


class Person():
    # state
    message = "Static state property"

    # constructure
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method
    def intruduce(self):
        print(f"{self.name} says: How dod you do?")

    def say_age(self):
        print(f"{self.name} says: I am {self.age} years old!!")

    @classmethod
    def expalin(cls):
        print("Static method property executed!!!")


person1 = Person("Justin", 25)
person2 = Person("Michael", 30)
person3 = Person("Harry", 28)

# Ordinary state
print("person1.name:", person1.name)

# Ordianry method
# Rodianry state belongs to each object
person1.intruduce()
person2.say_age()


print("==== Ordinary vs Static state =====")
# static state
# Static state belongs to The Class
# is a class attribute (often called static state).
new_message = Person.message
print("Ostatic state:", new_message)

# Static method
# Static method belongs to logically to the class, but it doesnt need a specific object(self).

Person.expalin()


print("==== Special/magic method ====")
# Python's msot common spacial methods are below:
# __init__ __new__ __str__ __call__ __getitem__ __eq__ __len__


class Car():
    # state
    description = "This calls makes cars!!!"

    # constructure
    # But __new__ is not used much coz it is already have inside the function
    def __new__(cls, *args):
        print("*__new__*")
        return super().__new__(cls)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    # methods

    def start_engine(self):
        print(f"The {self.name} started the engine!!!")

    def stop_engine(self):
        print(f"The {self.name} stopped the engine!!!")


new_car = Car("Ferrari", 2003)
new_car.start_engine()
new_car.stop_engine()
