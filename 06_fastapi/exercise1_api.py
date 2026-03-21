# Exercise 1 — Basic routes
# Create a FastAPI app with 3 GET endpoints:
# - `/` → returns your name and a welcome message
# - `/about` → returns a short bio dict
# - `/skills` → returns a list of your current skills


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def welcome():
    return {"name": "Sergiu", "message": "Welcome!"}


@app.get("/about")
def bio():
    return {
        "nationality": "Romanian",
        "age": 20,
        "city": "Sibiu"
    }


skills = ["mathematics", "sports"]


@app.get("/skills")
def my_skills():
    return {"skills": skills}
