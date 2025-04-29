from fastapi import FastAPI, HTTPException, status
from typing import Optional
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class updatepost(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

While True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Raila123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(2)


'''try:
    conn = psycopg2.connect(host='localhost', database = 'fastapi', user = 'postgres', password = '#7014martinSURE', cursor_factory = RealDictCursor)
    cursor = conn.cursor()
    print ("Database connection was successful!")
except Exception as error:
    print("Connecting to database failed")
    print("Error:", error)'''
my_posts = [
    {"id": 1, "title": "Post One", "content": "This is post one"},
    {"id": 2, "title": "Post Two", "content": "This is post two"},
]

def find_index_post(id):
    for index, post in enumerate(my_posts):
        if post['id'] == id:
            return index


@app.get("/posts")
def get_posts():
   posts = cursor.execute("""SELECT * FROM posts """)
   print(posts)
    return{"data": my_posts}

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI is working!"}

@app.put("/posts/{id}")
def update_post(id: int, post: updatepost):
    index = find_index_post(id)

    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {id} does not exist"
        )

    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {"data": post_dict}

