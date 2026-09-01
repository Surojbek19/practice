print("===== Operators =====")

# Operators: + - > >= < <= == is * /     // % += **

a = 19
b = 5

print("a > b:", a > b)
print("a/b:", a/b)

result = a//b
left = a % b
print("a//b bu qoldiqsiz bolish:", result)
print("a%b bu bo'linma qoldiqini ko'rsatadi:", left)

# a = a + 100 and a += 100 are the same thing
a = a + 100

print("a:", a)

print("a**2:", a**2)  # this a is multiplied a twice basicly  a2(a squared)
print("a**3:", a**3)  # this means a is musltiplied a three time a3(a cubed)

print("="*5)  # In Pyhton even a operator can be multiplied
print("D"*7)  # and even a letter can be multiplied


c = dict(name="Michael", age=32)
d = dict(name="Michael", age=32)
e = c
# In this case, paython comparese value of c and d objects but other languages it is usually compared their references
print("c == d:", c == d)
print(id(c), id(d))  # this is their references here, and they are different.

# this is how we check if the objects have same references. We use "is" operator!
print("c is d:", c is d)
# Now here "e" and "c" have same references, coz e equals c (e = c)
print("e is c:", e is c)


print("===== Conditions =====")
# Condistions doesn't check true or false but they check thruthy and falsey, coz they  are different things
x = 5
if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:  # else runs when all other coditions are not satisfied and else is considered none-conditional
    print("Case C")

print("====== Logical operators ======")
age = 23
# person = None

# if age > 13:
#     person = "adult"
# else:
#     person = "child"

# Ternery operator

# This done by using  ternery operator and it makes the logic more simplier.
person = "adult" if age > 18 else "minor"

print("person:", person)

print("********")
is_student = True
is_admin = False
is_guest = True
is_parent = True

if not is_student:
    print("Welcome here, do you wanna be a student?")
elif is_admin:
    print("Please go to the teachers' room!")
elif is_guest or is_parent:  # "or" makes it true even if there is one truthy value and others are falesy. But "and" makes it False even if there is only one falesy
    print("The waiting room is on the first floor!")
else:
    print("In other cases!!!")
