# A module is just a Python file. When you import it, you get access to everything inside it.

# Buit in modules = comes with Python ,no install needed


from utils.math_utils import multiply
import utils.string_utils
import utils
import math
import random
import os

# math
print(math.pi)  # 3.141592653589793
print(math.sqrt(16))  # 4.0
print(math.floor(3.7))  # 3
print(math.ceil(3.2))  # 4

# random
print(random.randint(1, 10))  # random numer 1-10 (including 1 and 10)
print(random.choice(["a", "b", "c"]))  # random item from list

# os
print(os.getcwd())  # current directory you're in
print(os.listdir("."))  # list files in current directory

# Import styles

# Style 1 - import the whole module
# import math
# math.sqrt(16) must prefix with math.

# Style 2 - import specific things from it
# from math import sqrt,pi
# sqrt(16)  no prefix needed

# Style 3 - import with alias (rename it)
# import math as m
# m.sqrt(16)

# Style 4 - import everything (avoid this)
# from math import * # pollutes your namespace, hard to debug
# sqrt(16)

# ------------------------------------------------

# Your own modules
# Any .py file you create is a module. You can import it into other files.

# import from utils.py

# print(utils.greet("Sergiu"))  # Hello, Sergiu!
# print(utils.add(3, 5))  # 8
# print(utils.PI)  # 3.14159

# Or with from
# from utils import greet, add


# Packages - folders of modules
# A **package** is a folder containing multiple modules

# my_project/
# │
# ├── main.py
# ├── utils/
# │   ├── __init__.py      ← makes it a package
# │   ├── math_utils.py
# │   └── string_utils.py

# __init__.py can be empty - it just tells Python "this folder is a package".


print(multiply(3, 4))  # 12


# Interesting fact to know

# import utils

# Then it gets ambiguous — and the **folder wins**
# because packages take priority over modules of the same name.

# my_project/
# ├── main.py
# ├── utils.py          ← loses if both exist
# ├── utils/
# │   ├── __init__.py   ← this makes it a package, package wins
# │   ├── math_utils.py
# │   └── string_utils.py

text = "hello world"
print(utils.string_utils.capitalize_words(text))  # Hello World
