from fastapi import FastAPI

app = FastAPI()


@app.get("/") '''Decorator'''
def root():

        return {"message": "Hello World"}


@app.get("/posts/vote") '''specifies a different path'''
def root():
    
    return()
