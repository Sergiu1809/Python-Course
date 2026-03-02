import math

x = 1
print(type(x))  # Output: <class 'int'>
x = 1.1
print(type(x))  # Output: <class 'float'>
x = 1+2j
print(x)  # Output: (1+2j)
print(type(x))  # Output: <class 'complex'>
print(x.real)  # Output: 1.0
print(x.imag)  # Output: 2.0


print(10 / 3)  # Output: 3.3333333333333335
print(10 // 3)  # Output: 3 returns an integer result (floor division)
print(10 ** 3)  # Output: 1000 exponentiation (10 raised to the power of 3)

x = -2.98
print(round(x))  # Output: -3 rounds to the nearest integer
print(abs(x))  # Output: 2.98 returns the absolute value
print(math.ceil(x))  # Outpu: -2 rounds up to the nearest bigger or equal integer
# Output: -3 rounds down to the nearest smaller or equal integer
print(math.floor(x))

# Type conversion
x = input("x: ")
x = int(x)  # Convert string input to an integer
print(x+1)  # Output: x + 1 (where x is the integer value entered by the user)

# Falsy values in Python
print(bool(0))  # Output: False
print(bool(0.0))  # Output: False
print(bool(""))  # Output: False
print(bool([]))  # Output: False
print(bool(()))  # Output: False
print(bool({}))  # Output: False
print(bool(None))  # Output: False
