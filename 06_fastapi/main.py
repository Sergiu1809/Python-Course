from fastapi import FastAPI

# Create the FastAPI app - this is your entire API
app = FastAPI()

# Define a route - this is an endpoint
# What is /?
# It's the path — the address of your endpoint. Think of it like a URL path:
# / specifically means the root — the homepage of your API.

# The decorator connects directly to the function immediately below it
# The decorator and the function are a pair — one decorator, one function, always.
# A decorator only applies to the one function directly below it

# The flow is:
# ```
# Browser hits http://127.0.0.1:8000/
#         ↓
# FastAPI sees: GET request, path "/"
#         ↓
# FastAPI finds: @app.get("/") → home()
#         ↓
# Runs home(), gets the return value
#         ↓
# Sends it back as JSON to the browser

# @app.get("/")
# This is a decorator — it tells FastAPI "when someone sends a GET request to the / path, run this function".


@app.get("/")
def home():
    return {"message": "Hello from my API!"}

# HTTP Methods — what they mean

# | Method | Purpose | Example |
# |---|---|---|
# | `GET` | Read data | get all tasks |
# | `POST` | Create data | create a new task |
# | `PUT` | Update data | update a task |
# | `DELETE` | Delete data | delete a task |

# uvicorn          → the server
# 06_fastapi.main  → the file (06_fastapi/main.py)
# :app             → the FastAPI instance inside that file
# --reload         → restart automatically when you save changes

# This is one of FastAPI's best features. While your server is running go to:
# http://127.0.0.1:8000/docs
# FastAPI automatically generates an interactive API documentation page.
# You can test your endpoints directly from the browser without writing any code.
# This is called Swagger UI and in real projects your frontend team uses this to understand your API.
