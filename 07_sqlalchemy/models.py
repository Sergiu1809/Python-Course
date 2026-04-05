# In a project that uses database, models are Python classes that represent
# your database tables. Instead of writing CREATE TABLE in SQL, you define
# a Python class and SQLAlchemy creates the table for you automatically.
# models.py is where all these classes live - one class per database table.
# models.py answers one question: "what does my database look like?"
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

# relationship is a Python-level connection between two models. It lets you
# navigate between related objects directly in Python.
from sqlalchemy.orm import relationship

# without relationship - you'd have to query manually
# user = db.query(User).filter(User.id == 1).first()
# tasks = db.query(Task).filter(Task.user_id == user.id).all()

# with relationship - automatic
# user = db.quey(User).filter(User.id == 1).first()
# tasks = user.tasks # <- just like accesing an attribute


# Base is the parent class all your models inherit from. It's  what tells
# SQLAlchemy "this Python class represents a database table". Without inheriting from
# Base, SQLAlchemy doesn't know about the class at all.

from database import Base

# The User model
# class User(Base) - User inherits from Base, making it a database model.


class User(Base):
    # __tablename__ special attribute recognized by SQLAlchemy
    # it tells the ORM: 'the database is named users'
    # without it: SQLAlchemy would try to guess the table name
    # __tablename__ = "users" - this is the actual table name in PostgreSQL.
    # The class is called User (singular, capital) but the table is called users
    # (plural, lowercase). This is the standard convention:
    # Python class -> Database table
    # User -> users
    # Task -> tasks
    # Product ->  products
    __tablename__ = "users"

    # Column(...) - defines this as a table column
    # Integer - is a whole number
    # primary_key = True - this is the unique identifier for each row,
    # auto-increments automatically (replaces SERIAL from raw SQL)
    # index = True - creates a database index, makes lookups by id faster
    id = Column(Integer, primary_key=True, index=True)
    # nullable = False -> same as NOT NULL in SQL - field is required
    name = Column(String, nullable=False)
    # unique = True -> same as UNIQUE in SQL - no duplicates allowed
    email = Column(String, unique=True, nullable=False)
    # no constraints on age and city - they're optional
    age = Column(Integer)
    city = Column(String)

    # This is purely a Python convenience - it adds no column to the database
    # It tells SQLAlchemy:
    # "a User has many Tasks - let me access them as user.tasks"
    # "Task" - the related model
    # back_populates="owner" - connects to the owner relationship in Task
    # making it bidirectional:
    # user.tasks -> list of all tasks belonging to this user
    # task.owner -> the user who owns this task
    tasks = relationship("Task", back_populates="owner")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    # default = False - when you create a task without specifying completed, it
    # automatically sets it to False. Same as DEFAULT FALSE in SQL.
    completed = Column(Boolean, default=False)
    # This is the foreign key - the actual column that links tasks to users.
    # Integer - stores a number
    # ForeignKey("users.id") - that number must match an existing id in the users table
    user_id = Column(Integer, ForeignKey("users.id"))
    #     tasks.user_id  →  must match  →  users.id
    #     (foreign key)                    (primary key)

    # Mirror of the tasks relationship in User:
    # "User" - the related model
    # back_populates="tasks" - connects back to tasks relationship in User
    owner = relationship("User", back_populates="tasks")
    # Together they form a bidirectional relationship:
    # From user -> get tasks
    # user.tasks # [task1, task2, task3]
    # From task -> get user
    # task.owner # User(name="Sergiu", ...)
    # task.owner.name # "Sergiu"

# Summary - three layers in this file
# Layer              What it does
# Column(...)        defines the actual database columns
# ForeignKey(...)    creates the database-level link between tables
# relationship(...)  Python convenience to navigate between objects

# The first two affect the real database. The third one only exxists in Python.
