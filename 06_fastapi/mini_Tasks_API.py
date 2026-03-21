from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for now ( no database yet)
tasks = []
next_id = 1  # auto-increment ID counter, like a real database would do

# Pydantic model - defines what data you EXPECT to receive
# When React sends JSON, FastAPI checks it matches this shape


class Task(BaseModel):
    title: str
    description: str = ""

# GET /tasks - React asks "give me all tasks"


@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}  # returns the entire list

# POST /tasks - React sends a new task to create


@app.post("/tasks")
def create_task(task: Task):  # FastAPI reads the JSON body and validates it against Task model
    global next_id  # access the counter outside the function
    new_task = {
        "id": next_id,  # assign an ID
        "title": task.title,  # take the title from the request
        "description": task.description,
        "completed": False  # new tasks always start as not completed
    }
    tasks.append(new_task)  # add to our "database"
    next_id += 1
    return new_task  # send the created task back to React

# GET/tasks/5 - React asks "give me task number 5"


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if (task["id"] == task_id):
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Delete /tasks/5 - React says "delete task number 5"


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return {"message": "Task_deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

# What HTTPException is
# raise HTTPException(status_code=404, detail="Task not found")
# This is how you return errors in FastAPI. Instead of returning a normal response you raise an exception with a status code and message.
#  FastAPI catches it and returns the proper HTTP error response automatically.


# The real world flow - step by step

# Let's say you're building a Todo app. A user adds a task:

# 1. User types "Buy groceries" in React and clicks Add

# 2. React sends:
# POST http://yourapi.com/tasks
# {"title": "Buy groceries"}

# 3. FastAPI receives it:
# -validates: does it have a title? is it a string?
# -creates the task object
# -saves to PostgreSQL database
# -gets back ID=42 from database

# 4. FastAPI responds:
# {"id": 42, "title": "Buy groceries", "completed": false}

# 5. React receives the response:
# -adds the task to the UI immediately
# - shows "Buy groceries" in the list

# The whole round trip takes miliseconds. The user sees their task appear instantly.

# WHY POSTMAN MATTERS HERE

# During development, your React frontend might not be built yet. Postman lets you
# test if your API works correctly before connecting the frontend:

# Without Postman: build API -> build React -> connect -> test -> find bug -> dont know if
# bug is in API or React

# With Postman: build API -> test with Postman -> confirm API works -> build React ->connect -> everything works
