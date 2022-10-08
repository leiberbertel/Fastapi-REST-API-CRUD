# Python
from datetime import datetime
from typing import Text, Optional
from uuid import uuid4 as uuid

#Pydantic
from pydantic import BaseModel, Field

# Fastapi
from fastapi import FastAPI, HTTPException

app =  FastAPI()

posts = []

# Post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    published: bool = False

@app.get('/')
def read_root():
    return {'Welcome': 'Welcome to my REST API'}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post: Post):
    post.id = str(uuid())
    posts.append(post.dict())
    return posts[-1]

@app.get('/posts/{post_id}')
def get_post(post_id):
    for post in posts:
        if post['id'] == post_id:        
            return post 
    else:
        return 'Not found'              
 