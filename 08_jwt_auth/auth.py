# date time gives the current time: -> 2026-03-24 21:00:00
# timedelta - represents a duration of time:
# timedelta(minutes=30) -> 30 minutes
# Together they calculate when the token expires:
# expire = datetime.utcnow() + timedelta(minutes=30)
# "right now" + "30 minutes" = "expires at 21:30:00"
from datetime import datetime, timedelta, timezone
# jose is the python-jose library installed. It handles everything JWT related:
# jwt - the main object with two methods you'll use:
# jwt.encode(payload, secret, algorithm) # create a token
# jwt.decode(token, secret, algorithm) # verify and read a token
# JWTError - an exception that gets raised when:
# token signature is invalid ( someone tampered with it)
# token has expired
# token is malformed
# try:
#     jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
# except JWTError:
#     # token is bad → reject the request
from jose import JWTError, jwt
# passlib is the password hashing library installed. CryptContext is its
# main class - it manages which hashing algorithm to use
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

# ── Password hashing setup ────────────────────────────────────
# CryptContext tells passlib which hashing algorithm to use
# bcrypt is the industry standard for password hashing
# "deprecated='auto'" means old hashes get upgraded automatically
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    # Takes a plain text password and returns a bcrypt hash
    # "mypassword123" -> "$2b$12$abcxyz..."
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Compares a plain text password against a stored hash
    # Returns True if they match, False if not
    # Used during login to check if the password is correct
    return pwd_context.verify(plain_password, hashed_password)

# ── JWT setup ─────────────────────────────────────────────────


# Secret key - used to sign and verify tokens
# In production this should be a long random string stored in .env
# Anyone with this key can create valid tokens - keep it secret
SECRET_KEY = os.environ.get("SECRET_KEY")

# Algorithm used to sign the token
# HS256 = HMAC with SHA-256 - industry standard for JWT
ALGORITHM = "HS256"

# How long a token stays valid
# After this time the token expires and the user must login again
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict) -> str:
    # data = whatever you want to store in the token
    # typically {"sub": email} where "sub" = subject = who the token belongs to
    to_encode = data.copy()

    # Calculate expiry time: current time + 30 minutes
    expire = datetime.now(timezone.utc) + \
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    # Add expiry to the payload
    to_encode.update({"exp": expire})

    # Sign and encode the token using SECRET_KEY and ALGORITHM
    # Returns the final JWT string
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> str:
    # Verifies a token and returns the email stored inside it
    # Raises an exception if token is invalid or expired
    try:
        # Decode the token - this verifies the signature and expiry automatically
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # Extract the email from the payload
        # "sub" is the standard JWT field for the subject (who the token belongs to)
        email: str = payload.get("sub")

        if email is None:
            raise JWTError()

        return email

    except JWTError:
        # Token is invalid, expired, or tampered with
        raise JWTError()


# The two parts of this file
# Part 1 - Password hashing
# hash_password() -> register: hash before saving to DB
# verify_password() -> login: check if password matches hash

# Part 2 - JWT tokens:
# create_access_token() -> login: generate token after password verified
# verify_token() -> protected endpoints: check if token is valid

# How they connect to the flow
# REGISTER:
# plain password -> hash_password() -> store hashed_password in DB

# LOGIN:
# plain password + stored hash -> verify_password() -> match
#                                                   -> create_access_token()
#                                                   -> return token to user

# PROTECTED ENDPOINT:
# token from request -> verify_token() -> get email -> find user in DB -> proceed
