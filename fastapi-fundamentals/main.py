from fastapi import FastAPI

app = FastAPI(title="FastAPI Fundamentals")

@app.get("/")
def home():
    return { 'message': "Hello World", 'ok': True }