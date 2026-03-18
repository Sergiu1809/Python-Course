from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for now ( no database yet)
tasks = []
next_id = 1
