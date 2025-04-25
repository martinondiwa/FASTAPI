from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class post(BaseModel):
    title: str
    content: str
    published : bool = True
    rating: Optional[int] = None
#Creating a storage for my posts
my_posts = [{"title": "title of post", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "I like pizza", "id": 2}]


@app.get("/")
async def root():
        return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return{"data": my_posts}

#@app.post("/createposts")
#def create_posts(payLoad: dict = Body(...)):
 #   print(payLoad)
  #  return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}

# title str, content str (General)
#@app.post("/createposts")
#def create_posts(new_post: post):
 #       print(new_post)
 #       return {"data": "new post"}

# title str, content str (Extracting the Title Only)
#@app.post("/createposts")
#def create_posts(new_post: post):
#           print(new_post.title)
#          return {"data": "new post"}

#Asigning optional property title str, content str (Extracting the Title Only)
#@app.post("/createposts")
#def create_posts(new_post: post):
                #print(new_post.published)
                #return {"data": "new post"}

#working with rating
#@app.post("/createposts")
#def create_posts(new_post: post): #   print(new_post.published)
#  return {"data": "new post"}

#pydantic modal storage capabilities 
#@app.post("/createposts")
#def create_posts(new_post: post):
 #   print(new_post)
  #  print(new_post.dict())
   # return {"data": new_post}

#following best practices (the paths should be ("/posts" , "/posts:id" , always in plural) with methods like (@app.post("/posts"), @app.get("/posts/{id}"),@app.get("/posts"), @app.put("/posts/{id}"), @app.delete("/posts/{id}")
@app.post("/posts")
def create_posts(new_post: post):
    print(new_post)
    print(new_post.dict())
    return {"data": new_post}
