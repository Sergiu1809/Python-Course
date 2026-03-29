# In a project that uses database, models are Python classes that represent
# your database tables. Instead of writing CREATE TABLE in SQL, you define
# a Python class and SQLAlchemy creates the table for you automatically.
# models.py is where all these classes live - one class per database table.
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
