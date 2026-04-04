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
