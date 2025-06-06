from fastapi import FastAPI, Request, HTTPException, status, Response
from typing import List

app = FastAPI()

my_posts = [
        {"id": 1, "title": "Post One", "content": "This is post one"},
        {"id": 2, "title": "Post Two", "content": "This is post two"},
        ]

#Deleting posts
def find_index_post(id: int):
    for i, p in enumerate(my_posts):
        if p ['id'] == id:
            return i

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    #deleting post
    # find the index in the array that has required ID
    #my_posts.pop(index)
    index = find_index_post(id)
    
    #handling errors due to non-existense ids
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    my_posts.pop(index)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
