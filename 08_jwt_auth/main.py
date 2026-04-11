# status - a collection of HTTP status code constants:
# without status - magic numbers, hard to read
# raise HTTPException(status_code = 401)
# with status - readable, self-documenting
# raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
# It's not required - 401 and status.HTTP_401_UNAUTHORIZED are identical.
# But status makes your code more readable and prevents typos.
from fastapi import FastAPI, HTTPException, Depends, status
# Those 2 handle the standard OAuth2 login flow.

# OAuth2PasswordBearer
# outh2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# Does two things:
# tells FastAPI where the login endpoint is - used by /docs to show an Authorize button
# automatically extracts the token from the Authorization header on every request:
# Request header:
# Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...
#                        ↑
#               oauth2_scheme extracts this part automatically
# Without it you'd have to manually read the header on every endpoint.

# OAuth2PasswordRequestForm
# def login(form_data: OAuth2PasswordRequestForm = Depends())
# A pre-built form that expects exactly two fields - userame(email) and password.
# This is the standard OAuth2 login format that all clients (Postman, browser, mobile apps)
# know how to send.

# It's why in /docs when you click login you see exactly two fields - username
# and password.
# FastAPI builds that form automatically from this class.
# form_data.username - the email the user typed
# form_data.password - the password the user typed
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic import BaseModel
from jose import JWTError
import models
import auth
from database import engine, get_db

# Creates all tables in PostgreSQL automatically
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ── OAuth2 setup ──────────────────────────────────────────────

# Tells FastAPI where the login endpoint is
# When a protected endpoint is called without a token
# FastAPI knows to redirect to "/login" to get one
oaut2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# ── Pydantic schemas ──────────────────────────────────────────

# defines what data comes IN when registering
# This is what the client sends in the request body
class UserCreate(BaseModel):
    name: str
    email: str
    password: str  # plain text - gets hashed before saving to DB
    # no id - doesn't exist yet, database generates it

# defines what data goes OUT in the response
# This is what we send back to the client
# without it, FastAPI would send everything back including hashed_password - a security disaster


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool  # no password - NEVER send password back, not even hashed
    # this is the security filter

    # Pydantic specifically looks for a class named Config inside your model
    # and reads its settings
    class Config:
        # by default Pydantic only reads from dictionaries like {"id": 1, "name": "Sergiu"}
        # SQLAlchemy returns objects with attributes like user.id, user.name
        # from_attributes = True tells Pydantic:
        # "you can also read from object attributes, not just dicts"
        # without this -> error when tryig to return a SQLAlchemy object
        from_attributes = True  # allows converting SQLAlchemy objects to Pydantic
        # "if you get an object instead of a dict, its attributes(user.id, user.name)
        # instead of dictionary keys (user['id'], user['name'])"

# defines what the login endpoint sends back after succesful login
# The client receives this and stores the access_token
# to use in future requests to protected endpoints


class Token(BaseModel):
    acces_token: str  # the JWT token string
    # looks like: "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJTZXJnaXUifQ.abc123"
    # client stores this and sends it with every protected request

    token_type: str  # always "bearer" - this is the OAuth2 standard
    # tells the client HOW to send the token
    # "bearer" means: put it in the Auth header like this:
    # Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...


# ── Dependency — get current logged in user ───────────────────

def get_current_user(
    token: str = Depends(oaut2_scheme),
    db: Session = Depends(get_db)
):
    # This function runs on every protected endpoint
    # It reads the token, verifies it, and returns the user

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Verify the token and extract the email
        email = auth.verify_token(token)
    except JWTError:
        raise credentials_exception

    # Find the user in the database by email
    user = db.query(models.User).filter(models.User.email == email).first()

    if user is None:
        raise credentials_exception

    return user  # returns the full User object to the endpoint
