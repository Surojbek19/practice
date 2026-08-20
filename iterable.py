print("==== Iterable object & RANGE")
# Iterable object in Python, it means any object or data collection in programming that can  give it iems one by one
# Itarable objects > string, dict, tuple, list, range, map, filter


text = "Michael"
for letter in text:  # here letter is a variable/refernece for each letter of the text vsrisble
    print(f"The letter: {letter}")


# [0, 3) range creates a range of numbers, which we often use with for loops.
range_obj = range(3)
print("range_obj:", range_obj)

for number in range_obj:
    print(f"The ranged number: {number}")

print("===== Dictionary =====")
# Dictionary (dicr) object in Python is an object that stores data as a key - value in pairs

# here we are basicly creating an object and both of them are doing same thing,
# they are creating obejct one person object, anoher one is person_obj but the second oneis most used
person = {"name": "Michael", "age": 32, "single": True}
person_obj = dict(name="Max", age=25, single=True)

print(f"Person: {person}")
print(f"Person_obj: {person_obj}")

# These two are doing same thing but the second oen is better becaus it is using get method and is more cnfortable
# if we ask hooby which doesnt exist in person this method returns error
name = person["name"]
print(f"The name: {name}")

# This method returns None id we ask hobby which diesnt exist in person
age = person.get("age")
hobby = person.get("hooby")
balance = person.get("balance", 0)  # this returns 0 as balance default value

print(f"Name: {name}, age: {age}, hobby: {hobby}, balance: {balance}")
print("The hobby:", hobby)
print(f"The age: {age}")

del person["single"]  # del operator reamove a state of the object
for item in person:
    print(f"Item: {item} => value: {person[item]}")
