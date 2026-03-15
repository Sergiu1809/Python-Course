# Output: True (lexicographical comparison) because "b" comes after "a" in the alphabet
print("bag" > "apple")

# if statement
temperature = 30
if (temperature > 25):
    print("It's a hot day")
elif (temperature > 20):
    print("It's a nice day")
else:
    print("It's not a hot day")

# ternary operator
age = 18
message = "Eligible to vote" if (age >= 18) else "Not eligible to vote"
print(message)  # Output: Eligible to vote

# Logical operators
is_raining = True
is_cold = False

if is_raining and is_cold:
    print("It's a bad day")
elif is_raining or is_cold:
    print("It's a bit bad day")
else:
    print("It's a good day")

is_cold = not is_cold  # Negation operator
print(is_cold)  # Output: True


# for loop
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# empty vector
array = [1, 7, 3, 4, 8, 3, 5]
for i in range(5):
    array.append(i)

# nested for loop to sort the array (bubble sort)
for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if (array[j] < array[i]):
            array[i], array[j] = array[j], array[i]
print(array)  # Output: [0, 1, 2, 3, 3, 4, 5, 7, 8]

for i in range(5):
    if (i % 2 == 0):
        # what if i want to print on same lane?
        print(i, end=" ")  # Output: 0 2 4
print()  # Move to the next line after the loop

shopping_cart = {
    "apple": 2,
    "banana": 3,
    "orange": 1
}

for item in shopping_cart:
    print(item)  # Output: apple, banana, orange (keys of the dictionary)

for item in shopping_cart.values():
    print(item)

x = 10
while x > 0:
    print(x, end=" ")  # Output: 10 9 8 7 6 5 4 3 2 1
    x -= 1
print()  # Move to the next line after the loop

command = ""
# while command != "quit":
#    command = input(">").lower().strip()

for i in range(1, 10):
    if i % 2 == 0:
        print(i)
