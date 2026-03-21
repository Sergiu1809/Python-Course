# Full CRUD - Build the Tasks API yourself from scratch without looking.
# Add one more endpoint:
# PUT /tasks/{task_id}/complete — marks a task as completed.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

next_id = 1
tasks = []


class Task(BaseModel):
    title: str
    description: str = ''


@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}


@app.post("/tasks")
def create_task(task: Task):
    global next_id
    new_task = {
        "id": next_id,
        "title": task.title,
        "description": task.description,
        "completed": False
    }
    tasks.append(new_task)
    next_id += 1
    return new_task


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if (task["id"] == task_id):
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if (task["id"] == task_id):
            tasks.pop(i)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    for task in tasks:
        if (task["id"] == task_id):
            task["completed"] = True
            return task
    raise HTTPException(status_code=404, detail="Task not found")
