from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"message": "Server is up and running"}}


@app.get("/about")
def about():
    return {"data": {"message": "This is the about page"}}
