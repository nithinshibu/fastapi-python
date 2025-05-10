# import the FAST API
from fastapi import FastAPI

# create an instance of the FastAPI
app = FastAPI()


# we are defining the path and get is called as operation and @app decorator is called as path operation decorator
@app.get('/')
#this function index is called as the path operation function

def index():
    return {'data':'blog list'}

# @app.get('/about')
# def about():
#     return {'data':'about page'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
    #fetch blog with id = id
    return {'data':id}

@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with id = id
    return {'data':{'1','2'}}
