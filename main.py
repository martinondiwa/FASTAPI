from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange 

app = FastAPI()

class post(BaseModel):
    title: str
    content: str
    published : bool = True
    rating: Optional[int] = None
#Creating a storage for my posts
my_posts = [{"title": "title of post", "content": "content of post 1", "id": 1}, {"title": "favourite foods", "content": "I like pizza", "id": 2}]

#Keep in mind this is not the best way of retrieving posts. (works with yX)
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

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
#@app.post("/posts")
#def create_posts(new_post: post):
 #   print(new_post)
  #  print(new_post.dict())
   # return {"data": new_post}


#Communicating with the frontend
@app.post("/posts")
def create_posts(post: post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


#Retrieving one individual post. 
#@app.get("/posts/{id}")
#def get_post(id):
 #   print(id)
#  return {"post_detail": f"Here is post {id}"}

#Getting the latest post
#@app.get("/posts/latest")
#def get_latest_post():
 #   post = my_posts[len(my_posts)-1]
   # return {"detail": post}


#works with yx usable though not best practice
#@app.get("/posts/{id}")
#def get_post(id: int):
   # print(type(id)) -(used to check the type of id)

 #   post = find_post(int(id))
  #  print(post)
   # return {"post_detail": post}

#manipulating the  error response- (script when only response is imported)
#@app.get("/posts/{id}")
#def get_post(id: int, response:Response):
    
 #   post = find_post(int(id))
  #  if not post:
   #     response.status_code = 404
   # return {"post_detail": post}

#error script when status is imported
#@app.get("/posts/{id}")
#def get_post(id: int, response:Response):

 #   post = find_post(int(id))
  #  if not post:
   #     response.status_code = status.HTTP_404_NOT_FOUND
    #    return {'message': f"post with id: {id} was not found"}
   # return {"post_detail": post}

#passing an error using HTTPException
@app.get("/posts/{id}")
def get_post(id: int, response:Response):
    
    post = find_post(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail = f"post with id: {id} was not found")
        return {"post_detail": post}
