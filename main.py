from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class post(BaseModel):
    title: str
    content: str

@app.get("/")
async def root():
        return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return{"data": "This is your posts"}

#@app.post("/createposts")
#def create_posts(payLoad: dict = Body(...)):
 #   print(payLoad)
  #  return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}

# title str, content str 
@app.post("/createposts")
def create_posts(new_post: post):
        print(new_post)
            return {"data": "new post"}
