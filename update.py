from fastapi import FastAPI, Request, HTTPException, status, Response
from typing import List
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class updatepost(BaseModel):
    title: str
    content: str
    published : bool = True
    rating: Optional[int] = None

my_posts = [
        {"id": 1, "title": "Post One", "content": "This is post one"},
        {"id": 2, "title": "Post Two", "content": "This is post two"},
        ]

@app.put("/posts/{id}")
def update_post(id: int, post: updatepost):
    print(updatepost)
    return {'message': "updated post"}
