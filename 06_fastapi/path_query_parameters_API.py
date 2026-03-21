# Exercise 2 — Path & query params
# Create an endpoint `GET /multiply/{number}`
# that multiplies the number by a query param `factor` (default 2).

from fastapi import FastAPI

app = FastAPI()


@app.get("/multiply/{number}")
def multiply(number: int, factor: int = 2):
    return {"result": number * factor}
