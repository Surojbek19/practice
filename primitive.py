print("===== number =====")
# In JAVA, variables are a name of storage location
# in Python, variables are named refrence

count = 100
count_type = type(count)
print(f"the count: {count} and count_type: {count_type} ")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)


print("====== String =======")
# METHODS: upper(), lower(), title(), find(), replace()

course = "AI Python FullStack"
result = type(course)
print(f"the reuslt (1): {result}")

result = course.title()
print(f"the reuslt (2): {result}")

result = course.upper()
print(f"the reuslt (3): {result}")

result = course.replace("FullStack", "MasterClass")
print(f"the reuslt (4): {result}")
print(course)

print("===== boolean =====")
# Functions > type(), input(), bool(), int(), str()

y = input("Give your value for y:")
print("y:", y)

result = y.isnumeric()

print(f"The input value is numeric: {result}")

# TRUTHY vs FALSY
# TRUTHY: True  100  -100  "MIT"
# FALSY: False  0  ""  None

test_falsy = ""  # "", False, 0, None (All of these are falsy value)
print("The test_falsy:", bool(test_falsy))

test_truthy = "Hello"  # "MIT", 65, True, -23 (All of these truthy value)
print("The test_truthy:", bool(test_truthy))
