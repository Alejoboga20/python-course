from fastapi import FastAPI

app = FastAPI(title="FastAPI Fundamentals")

BLOG_POST = [
    {"id": 1, "title": "Hello from FastAPI",
        "description": "First App using FastAPI"},
    {"id": 2, "title": "Hello from NestJS",
        "description": "First App using NestJS"},
    {"id": 3, "title": "Hello from Rails", "description": "First App using Rails"},
]


@app.get("/")
def home():
    return {'message': "Hello FastAPI", 'ok': True}


@app.get("/posts")
def list_posts():
    return {"data": BLOG_POST}
