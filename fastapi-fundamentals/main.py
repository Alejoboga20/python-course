from fastapi import FastAPI, Query, Body, HTTPException

app = FastAPI(title="FastAPI Fundamentals")

BLOG_POSTS = [
    {"id": 1, "title": "Hello from FastAPI",
        "content": "First App using FastAPI"},
    {"id": 2, "title": "Hello from NestJS",
        "content": "First App using NestJS"},
    {"id": 3, "title": "Hello from Rails", "content": "First App using Rails"},
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


@app.get("/posts/{post_id}")
def get_post(post_id: int, include_content: bool = Query(default=False, description="Include content of the post")):
    for post in BLOG_POSTS:
        if post["id"] == post_id:
            if not include_content:
                post = post.copy()
                post.pop("content")

            return {"data": post}

    raise HTTPException(status_code=404, detail="Post not found")


@app.post("/posts")
def create_post(post: dict = Body(...)):
    if "title" not in post or "content" not in post:
        raise HTTPException(
            status_code=404, detail="Title and Content are required")

    if not str(post["title"]).strip():
        raise HTTPException(
            status_code=404, detail="Title should not be empty")

    new_id = (BLOG_POSTS[-1]["id"] + 1) if BLOG_POSTS else 1
    new_post = {"id": new_id,
                "title": post["title"], "content": post["content"]}

    BLOG_POSTS.append(new_post)

    return {"data": new_post, "message": "new post created"}
