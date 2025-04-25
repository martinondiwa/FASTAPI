from main import app
from fastapi import FastAPI,request

app = FastAPI()

#Deleting posts
def find_index_post(id):
    for i, p in enumarate (my_posts):
        if p ['id'] == id:
            return i

@app.delete("/posts/{id}")
def delete_post(id: int):
    #deleting post
    # find the index in the array that has required ID
    #my_posts.pop(index)
    index = find_index_post(id)

    my_posts.pop(index)

    return {"message": "was successfully deleted"}
