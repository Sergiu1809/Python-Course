def hello(x):
    print("Hello" + " " + x + "!")


def sum(a, b):
    return a+b


hello("World")
print(sum(7.44, 2.56))

# optional parameters


def product(a, b=1):
    return a*b


def multiply1(*numbers):
    result = 1
    for i in range(len(numbers)):
        result *= numbers[i]
    return result


def multiply2(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def write(*strings):
    for string in strings:
        print(string)


multiply1(2, 3, 4)  # Output: 24
multiply2(2, 3, 4)  # Output: 24
write("Hello", "World", "Python", "Programming")

print(product(5))  # Output: 5 (b takes the default value of 1)
print(product(5, 3))  # Output: 15 (b takes the value of 3)
