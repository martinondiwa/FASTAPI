from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
        return {"message": "Hello World"}


def get_posts():
    return{"data": "This is your posts"}
