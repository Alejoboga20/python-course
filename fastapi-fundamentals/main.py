from fastapi import FastAPI, Query

app = FastAPI(title="FastAPI Fundamentals")

BLOG_POSTS = [
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
def list_posts(title: str | None = Query(default=None, description="Text to search by title")):
    if title:
        posts = [
            post for post in BLOG_POSTS if title.lower() in post["title"].lower()
        ]

        return {"data": posts, "query": {"title": title}}

    return {"data": BLOG_POSTS}
