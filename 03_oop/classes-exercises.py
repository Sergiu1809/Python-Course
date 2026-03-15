# Create a Car class with attributes: brand, model, year, speed (starts at 0).
# Add methods: accelerate(amount), brake(amount), describe(). Speed can't go below 0.

class Car:
    def __init__(self, brand, model, year, speed):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    def accelerate(self, amount):
        if (amount <= 0):
            print("Invalid amount.")
        else:
            self.__speed += amount
            print(f"Speed: {self.__speed}")

    def brake(self, amount):
        if (amount <= 0):
            print("Invalid amount.")
        else:
            self.__speed -= amount
            print(f"Speed: {self.__speed}")

    def describe(self):
        print(
            f"Brand: {self.__brand} \nModel: {self.__model} \nYear: {self.__year} \nSpeed: {self.__speed}")


# car = Car("Porsche", "GT3 RS", 2025, 0)
# car.accelerate(100)
# car.brake(50)
# car.describe()

# Create a Student class with name, grade (list of scores).
# Add methods: add_grade(score), average(), is_passing() (True if average ≥ 50)
class Student:
    def __init__(self, name, grades=None):
        self.__name = name
        self.__grades = grades if grades is not None else []

    def add_grade(self, score):
        if (score < 0 or score > 100):
            print("Invalid score")
        else:
            self.__grades.append(score)
            print(f"Nota adaugata: {score}")

    def average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def is_passing(self):
        return self.average() >= 50


# student = Student("Sergiu", [90, 87, 100])
# student.add_grade(80)
# print(student.average())
# print(student.is_passing())


# Create a base class Employee with name, salary. Add a method get_info(). Then create two child classes:
# Developer — add attribute language (e.g. "Python"), override get_info() to include it
# Manager — add attribute team_size, override get_info() to include it

class Employee:
    def __init__(self, name, salary):
        # single underscore — accessible by children (equivalent to protected in c++)
        self._name = name
        self._salary = salary

    def get_Info(self):
        print(f"Name: {self._name} Salary: {self._salary}")


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self._language = language

    def get_Info(self):
        print(
            f"Name: {self._name} Salary: {self._salary} Language: {self._language}")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self._team_size = team_size

    def get_Info(self):
        print(
            f"Name: {self._name} Salary: {self._salary} Team size: {self._team_size}")


developer = Developer("Sergiu", 5000, "Python")
manager = Manager("Ionut", 7000, 10)

developer.get_Info()
manager.get_Info()

# Build a mini Library system:
# Book class: title, author, is_available (True by default)
# Library class: has a list of books, methods
# add_book(book)
# borrow_book(title) — marks book as unavailable
# return_book(title) — marks book as available
# show_available() — prints all available books


class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._is_available = True

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def is_available(self):
        return self._is_available

    def borrow(self):
        self._is_available = False

    def return_book(self):
        self._is_available = True


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        print(f"Added: {book.get_title()}")

    def borrow_book(self, title):
        for book in self._books:
            if book.get_title() == title:
                if book.is_available():
                    book.borrow()
                    print(f"Borrowed: {title}")
                else:
                    print(f"'{title}' is not available.")
                return
        print(f"{title} not found.")

    def return_book(self, title):
        for book in self._books:
            if (book.get_title() == title):
                book.return_book()
                print(f"Returned: {title}")
                return
        print(f"'{title}' not found.")

    def show_available(self):
        available = [book for book in self._books if book.is_available()]

        if not available:
            print("No books available.")
        else:
            for book in available:
                print(f"- {book.get_title()} by {book.get_author()}")


library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("Dune", "Frank Herbert"))
library.add_book(Book("Clean Code", "Robert Martin"))

library.show_available()   # all 3 books
library.borrow_book("Dune")
library.show_available()   # 1984 and Clean Code
library.return_book("Dune")
library.show_available()   # all 3 again
