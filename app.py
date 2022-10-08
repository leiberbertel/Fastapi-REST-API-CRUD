from fastapi import FastAPI

app =  FastAPI()

posts = []


@app.get('/')
def read_root():
    return {'Welcome': 'Welcome to my REST API'}

@app.get('/posts')
def get_posts():
    return posts

@app.post('/posts')
def save_post(post):
    print(post)
    return 'received'