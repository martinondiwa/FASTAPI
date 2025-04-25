
from fastapi import FastAPI, Request, HTTPException, status, Response
from typing import List
from pydantic import BaseModel


app = FastAPI()

class post(BaseModel):
    title: str
    content: str
    published : bool = True
    rating: Optional[int] = None

my_posts = [
        {"id": 1, "title": "Post One", "content": "This is post one"},
        {"id": 2, "title": "Post Two", "content": "This is post two"},
        ]
                                ]

