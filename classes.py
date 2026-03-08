# Step 1: Classes & Objects

class Dog:
    pass  # empty class for now


# Creating objects (instances) from the class
dog1 = Dog()
dog2 = Dog()

print(type(dog1))  # <class '__main__.Dog'>
print(dog1 == dog2)  # False - they-re different objects


# Step 2: __init__ & Instance Variables & Default parameters

class Dogv2:
    #  __init__ is the constructor — it runs automatically when you create an object. It's where you define the object's attributes (its data).

    # default parameters, RULE: required parameters first, optional(default) last.
    def __init__(self, name="Unknown", age="0", bread="Mixed"):
        self.name = name
        self.age = age
        self.bread = bread

    # self = the object itself. It's how the object refers to its own data.


# You can also add and modify attributes after creation (if attributes are public)
dog3 = Dogv2()

print(dog3.name)  # Unknown
dog3.name = "Max"
print(dog3.name)  # Max

# Step 3: Methods


class Dogv3:

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Method - always takes self as first parameter

    def bark(self):
        print(f"{self.name} says: Wolf!")

    def describe(self):
        print(f"{self.name} is {self.age} years old")

    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! Now {self.age} years old.")


dog4 = Dogv3("Max", 3, "Husky")

dog4.bark()  # Rex says: Woof!
dog4.describe()  # Rex is 3 years old
dog4.have_birthday()  # Happy birthday Rex! Now 4 years old.

# Class variables vs Instance variables


class Dogv4:
    # Class variable - shared by ALL dogs
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age


dog5 = Dogv4("Rex", 3)
dog6 = Dogv4("Bella", 5)

print(dog5.species)  # Canis familiaris
print(dog6.species)  # Canis familiaris
print(Dogv4.species)  # Canis familiaris - access from class directly

# Step 4: Encapsulation
# Controlling acces to data. Hiding internal details from the outside.


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # __ = private, can't access directly

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")

    def get_balance(self):  # controlled acces via method
        return self.__balance


acc = BankAccount("Sergiu", 2000)

acc.deposit(500)  # Deposited 500. New balance: 2500
acc.withdraw(200)  # Withdrew 200. New balance: 2300

# This CRASHES - private variable
# print(acc.__balance) Attribute Error

# This works - using the method
print(acc.get_balance())  # 2300

# Why encapsulation matters" You protect data from being changed in ways you dont expect.
# The balance can only be changed through deposit() and withdraw(), which have validation logic.

# Step 5: Inheritance
# A class can inherit from another class - getting all its attributes and methods for free


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child class - inherits from Animal


class Dogv5(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # call parent's __init__
        self.breed = breed  # add extra attributes

    def bark(self):
        print(f"{self.name} saus: Woof!")


class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor

    def meow(self):
        print(f"{self.name} says: Meow!")


dog7 = Dogv5("Rex", 3, "Labrador")
cat = Cat("Whiskers", 2, True)

dog7.eat()  # Inherited from Animal - Rex is eating.
dog7.sleep()  # Inherited from Animal - Rex is sleeping.
dog7.bark()  # Dog's own method

cat.eat()  # Inherited from Animal
cat.meow()  # Cat's pwn method

# Overriding methods
# A child can replace a parent method

# class Animal:
#    def speak(self):
#       print("Some generic animal sound")

# class Dog(Animal):
#    def speak(self):            # overrides parent
#        print("Woof!")

# class Cat(Animal):
#    def speak(self):            # overrides parent
#        print("Meow!")

# animal = Animal()
# dog = Dog()
# cat = Cat()

# animal.speak()  # Some generic animal sound
# dog.speak()     # Woof!
# cat.speak()     # Meow!


# Step 6: Polymorphism
# Same method name, different behavior depending on the object. It,s the payoff of inheritence.

class Shape:
    def area(self):
        pass  # to be overridden


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Polymorphism in action


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    print(f"{shape.__class__.__name__}: area = {shape.area()}")

# Circle: area = 78.5
# Rectangle: area = 24
# Triangle: area = 12.0

# Same .area() call - completely different behavior per object. This is the power of polymorphism
