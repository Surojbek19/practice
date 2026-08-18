print("===== number =====")
# In JAVA, variables are a name of storage location
# in Python, variables are named refrence

count = 100
count_type = type(count)
print(f"the count: {count} and count_type: {count_type} ")

result1 = count.bit_count()  # method
result2 = count.numerator  # state
print(result1, result2)
