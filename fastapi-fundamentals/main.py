from http import HTTPStatus
from typing import List, Optional, Union, Literal

from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="FastAPI Fundamentals")


class Tag(BaseModel):
    name: str = Field(..., min_length=2, max_length=20, description="Tag")


class Author(BaseModel):
    name: str = Field(..., min_length=3, max_length=20, description="Author")


class PostBase(BaseModel):
    title: str
    content: Optional[str] = None
    tags: Optional[List[Tag]] = Field(default_factory=list)
    author: Author


class PostCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=5, max_length=50,
        description="Post Titlte",
        json_schema_extra={"example": "This is a content"}
    )
    content: Optional[str] = Field(
        default="",
        min_length=0,
        max_length=1000,
        json_schema_extra={"example": "This is a content"},
    )
    author: Author = Field(
        ...,
        json_schema_extra={"example": "Author of the post"},
    )
    tags: list[Tag] = Field(default_factory=list)

    @field_validator("title")
    @classmethod
    def not_allowed_title(cls, value: str) -> str:
        if "spam" in value.lower():
            raise ValueError("Title can not contain word: spam")

        return value


class PostPublic(PostBase):
    id: int


class PostSummary(BaseModel):
    id: int
    title: str


class PostUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=5, max_length=50)
    content: Optional[str] = None


BLOG_POSTS: List[PostPublic] = [
    PostPublic(id=1, title="Hello from FastAPI",
               content="First App using FastAPI", author=Author(name="Alejo")),
    PostPublic(id=2, title="Hello from NestJS",
               content="First App using NestJS", author=Author(name="Daniel")),
    PostPublic(id=3, title="Hello from Rails",
               content="First App using Rails", author=Author(name="Boga")),
]


@app.get("/")
def home():
    return {'message': "Hello FastAPI", 'ok': True}


@app.get("/posts", response_model=List[PostPublic])
def list_posts(title: Optional[str] = Query(default=None,
                                            alias="search",
                                            min_length=5,
                                            max_length=50,
                                            description="Text to search by title",
                                            ),
               limit: int = Query(default=10, ge=1, le=50,
                                  description="Number of post to be returned"),
               offset: int = Query(default=0, ge=0, le=50,
                                   description="Amount of skipped posts"),
               order_by: Literal["id", "title"] = Query(
        default="title", description="Order by id or title"),
        direction: Literal["asc", "desc"] = Query(default="asc")
):

    print(
        f"title {title}, limit {limit}, offset {offset}, order_by {order_by}, direction {direction}")

    results = BLOG_POSTS

    if title:
        results: List[PostPublic] = [
            post for post in results if title.lower() in post.title.lower()
        ]

    results = sorted(
        results, key=lambda post: post.id if order_by == "id" else post.title, reverse=(direction == "desc"))

    return results[offset: offset + limit]


@app.get("/posts/{post_id}", response_model=Union[PostPublic, PostSummary])
def get_post(post_id: int = Path(..., ge=1, title="Post ID", description="Id must be grater than 1", example=1),
             include_content: bool = Query(default=False, description="Include content of the post")):
    for post in BLOG_POSTS:
        if post.id == post_id:
            if not include_content:
                post_summary = PostSummary(id=post.id, title=post.title)
                return post_summary
            return post

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                        detail="Post not found")


@app.post("/posts")
def create_post(post: PostCreate):
    new_id = (BLOG_POSTS[-1].id + 1) if BLOG_POSTS else 1
    new_post = PostPublic(id=new_id, title=post.title, content=post.content,
                          author=Author(name=post.author.name),
                          tags=[
                              Tag(name=tag.name) for tag in post.tags])

    BLOG_POSTS.append(new_post)

    return {"data": new_post, "message": "new post created"}


@app.put("/posts/{post_id}")
def update_post(post_id: int, data: PostUpdate):

    for post in BLOG_POSTS:
        if post_id == post.id:
            payload = data.model_dump(exclude_unset=True)

            if "title" in payload:
                post.title = payload["title"]
            if "content" in payload:
                post.content = payload["content"]
            return {"message": "Post updated", "data": post}

    raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                        detail="Post not found")


@app.delete("/posts/{post_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_post(post_id: int):
    for index, post in enumerate(BLOG_POSTS):
        if post.title == post_id:
            BLOG_POSTS.pop(index)

            return
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                        detail="Post not found")
