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
