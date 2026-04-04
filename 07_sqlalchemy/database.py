# This file sets up the database connection. Every other file imports from here
# creates the actual connection to PostgreSQL.
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base  # creates the Base
# class that all your models inherit from. It's what makes a Python class
# become a database table.
# creates a factory for database sessions.
from sqlalchemy.orm import sessionmaker
# A session is like a workspace - you open it, do your database operations, then close it.
from dotenv import load_dotenv
import os  # needed to read environment variables after load_dotenv() loads them

load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")

# The engine - the actual connection to PostgreSQL
# echo = True prints all SQL to terminal so you can see what's happening
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal - a factory that creates database sessions
# Each request gets its own session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base - all your models will inherit from this
Base = declarative_base()

# Dependancy - gives each endpoint its own database session
# automatically closes it when the request is done

# A session is a temporary workspace between your code and the database. Think of it like opening a Google Doc:

# you open it
# make your changes
# save and close it


def get_db():
    db = SessionLocal()
    try:
        # yield — gives value and PAUSES the function
        # resumes after the endpoint finishes
        yield db  # Yield pauses a function's execution and returns a value temporarily
    finally:  # finally always runs — even if the endpoint crashes with an error:
        db.close()
