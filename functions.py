print("====== DEFINE vs CALL ======")
# built in functions > print(), type()
# Functions - reusable block of code!
# in Puthon we don't need {} curly parentheses like in JS

# DEFINE - build


def greet(a):  # a is the paremetr of function / This is a void function, that's why result1 get None (in JS it is undefined)
    print(f"How are you {a}")


def greeting(b):  # b is the paremetr of function / This function retuns value that's why result2 doesnt get None
    print("The function is executed!!!")
    return f"Hi {b}"


# CALL - execute
result1 = greet("Martin")  # Martin is the argument of the function
print(result1)

result2 = greeting("Michael")  # Michael is the argument of the function
print(result2)
