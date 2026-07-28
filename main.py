from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello Railway!"
    }


@app.get("/about")
def about():
    return {
        "app": "FastAPI Demo",
        "status": "Running"
    }
