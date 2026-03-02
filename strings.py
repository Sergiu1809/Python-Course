course = "Python Programming"
print(course[0])  # Output: P
print(course[1])  # Output: y
print(len(course))  # 18
print(course[0:6])  # Output: Python
print(course[7:])  # Output: Programming
print(course[:6])  # Output: Python
print(course[-1])  # Output: g
print(course[:])  # Output: Python Programming

first = "John"
last = "Smith"
full_option1 = first + " " + last
full_option2 = f"{first} {last}"
print(full_option1)  # Output: John Smith
print(full_option2)  # Output: John Smith

methods = "Python Methods"
print(methods.upper())  # Output: PYTHON METHODS
print(methods.lower())  # Output: python methods
print(methods.title())  # Output: Python Methods
print(methods.find("o"))  # Output: 4
print(methods.find("Met"))  # Output: 7
print(methods.find("Z"))  # Output: -1
print(methods.find("p"))  # Output: -1 (case-sensitive)
print(methods.replace("o", "0"))  # Output: Pyth0n Meth0ds
# Output: Python Methods (no change since "0" is not in the original string)
print(methods.replace("0", "o"))
print(methods.replace("Python", "Java"))  # Output: Java Methods
print("Python" in methods)  # Output: True
print("Java" in methods)  # Output: False
print("c++" not in methods)  # Output: True

input_string = "   Hello World!   "
print(input_string.strip())  # Output: Hello World!
print(input_string.lstrip())  # Output: "Hello World!   "
print(input_string.rstrip())  # Output: "   Hello World!"
