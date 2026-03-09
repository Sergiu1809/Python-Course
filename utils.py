def greet(name):
    return f"Hello, {name}!"


def add(a, b):
    return a+b


PI = 3.14159


if __name__ == "__main__":
    # this block is invisible to anyone who imports this file
    print("Testing greet:")
    print(greet("Sergiu"))

# Think of it as a "tun rhis only if I'm the one being executed" check.
# In real projects every file that has test/demo code at the bottom should
# have this guard - otherwisw importing it anywhere creates unwanted side effects
