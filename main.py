from fastapi import FastAPI

app = FastAPI()


@app.get("/") '''specifies a different path'''
def root():
    
    return {"message": "Get your voote"}
