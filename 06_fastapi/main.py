from fastapi import FastAPI
from pydantic import BaseModel

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

# run "uvicorn 06_fastapi.main:app --reload" in terminal


@app.get("/")
def home():
    return {"message": "Hello from my API!"}
# http://127.0.0.1:8000

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


@app.get("/users/{user_id}")
def get_user(user_id: int):  # no ": int" -> treats it like a string
    return {"user_id": user_id, "name": "Sergiu"}
# http://127.0.0.1:8000/users/42

# user_id: int - FastAPI automatically validates the type. If you go to /users/abc it
# return a validation error automatically. No extra code needed

# Query parameters(?)
# Parameters that come after ? in the URL:


@app.get("/search")
def search(query: str, limit: int = 10):
    return {"query": query, "limit": limit}
# http://127.0.0.1:8000/search?query=python&limit=5

# limit: int = 10 means it's optional - defaults to 10 if not provided

# --------------------------- Request body with POST--------------------------------

# For POST requests you send data in the body, not the URL. FastAPI uses Pydantic
# models to define and validate this data:


class Task(BaseModel):
    title: str
    description: str = ''  # optional, defaults to empty string
    completed: bool = False  # optional, defaults to False


@app.post("/tasks")
def create_task(task: Task):
    return {
        "message": "Task created",
        "task": task
    }

# FastAPI automatically:
# - reads the JSON body
# - validates every field
# - converts types
# - returns clear errors if something is wrong

# The key difference in how you send them

# GET -> data travels in the URL
# POST -> data travels in the body (hidden, not in the URL)

# GET — data in URL, visible to everyone
# GET /search?query=python&limit=10

# GET — data in URL, visible to everyone
# GET /search?query=python&limit=10

# POST — data in body, not visible in URL
# POST /tasks
# body: {"title": "Learn FastAPI", "description": "..."}

# This is why POST is used for sensitive things like login:
# You'd never want this:
# GET /login?password=123456 # ❌ password visible in URL, stored in browser history

# Always this instead:
# POST /login
# body: {"email": "...", "password": "123456" } #hidden in the body
