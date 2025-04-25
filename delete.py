from main import app
from fastapi import FastAPI, Request, HTTPException

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

#@app.get("/posts/{id}")
#def get_post(id: int):

 #   post = find_post(id)
  #  if not post:
   #     raise HTTPException(status_code=status.HTTP_204_NO_CONTENT)
                    

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    #deleting post
    # find the index in the array that has required ID
    #my_posts.pop(index)
    index = find_index_post(id)

    my_posts.pop(index)

    return {"message": "was successfully deleted"}
