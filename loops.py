print("===== for operator ======")
# Iterable objects > string dict tuple list range map filter

text = "MIT"
numbs = [1, 4, 2, 6, 9]
car_obj = dict(brand="Ferrari", year=1991)
range_obj = range(5)  # in range, the last number(5) wont be  included

for letter in text:
    print("letter:", letter)

print("---------")

for number in numbs:
    print("number:", number)

print("---------")

for key in car_obj:
    print(f"the key: {key} => value: {car_obj.get(key)}")

print("---------")

for x in range_obj:
    print("x:", x)


print("===== break/else =====")
# "break" stops the process/loop. In this case, loop stops if y bigger than 30
# this starts with 1 and skipes 5 numbers and next number is 6 nad same 11, 16.
for y in range(1, 49, 5):
    print("y:", y)
    if y > 30:
        print("break stops the porcess/loop")
        break
else:
    print("Executed successfully!")
    # Here "else" works if break doesnt stop the loop/process.


print("==== while =====")
# we use "while" when we dont know how many time loop runs.
# Basicaly, we use "while" when repeatition should continue until a condition changes.
# we use "for" when we exactly know numbur of repeation. Ex: "MIT", "for runs 3 times and stops"
numb = 40

while numb > 0:
    numb -= 10
    print(f"the numb equels {numb}")

print("------")
count = 0
while True:
    count += 1
    x = int(input("Find the number: "))

    if x == 41:
        print(f"You found the number in {count}")
        break
    else:
        print("Wrong! Try again!")
