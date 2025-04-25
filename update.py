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

def find_index_post(id):
    for index, post in enumerate(updatepost):
        if post['id'] == id:
            return index

@app.put("/posts/{id}")
def update_post(id: int, post: updatepost):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
        post_dict = updatepost.dict()
        post_dict['id'] = id
        my_posts[index] = post_dict
        return {"data": post_dict}
