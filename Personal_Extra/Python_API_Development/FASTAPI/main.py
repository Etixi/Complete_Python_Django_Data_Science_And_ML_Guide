from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import uvicorn

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

app = FastAPI()

# request Get method uri: "/"

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


# http://127.0.0.1:8000/docs#/default/create_posts


# @app.post("/createposts")
# def create_posts(payload: dict = Body(...)):
#    print(payload)
#    return {"new_post": f"title{payload['title']} content: {payload['content']}"}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post.rating)
    return {"data": "new post"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
