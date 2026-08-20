import array  # package/model
import math
# we can import one specific or more method from one package
from math import ceil, asin

print("==== What is object in Python =====")
# An object has state (name, age,..) and method (all action that can be doen by the object) properties.
# Everything is object in Python. Every object belongs to a type/class and that class defines what that object can do!

print(type("HEllo World!!!"))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigmas > Functional Programming & OOP
# OOP 4 consepts > Encapsulation, Abstraction, Inheritance, and Polymorphism
result1 = math.ceil(97.7)
print(result1)


print("==== Error handlig syste ====")

car_obj = dict(name="Tayota", year=2024, electric=False)

try:
    print("Passed here!!!")
    a = car_obj.speed
    # here error happens so this line and other belove lines dont work
    result = car_obj["country"]
    print("result:", result)
except KeyError as err:
    # if ther is no error, then this line doesnt work
    print("This kind of object key doesnt exsit:", err)
else:
    # if everything works fine, then this line works
    print("Execution completed!!!")

finally:
    # this line works with or without error case
    print("Final closing logic!!!")
