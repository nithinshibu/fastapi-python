# import the FAST API
from typing import Optional
from fastapi import FastAPI

# create an instance of the FastAPI
app = FastAPI()


# we are defining the path and get is called as operation and @app decorator is called as path operation decorator
@app.get('/')
#this function index is called as the path operation function

def index():
    return {'data':'blog list'}


#handle the query parameters
#here limit and published are query parameter
#here we are also giving default values
#suppose we need an optional paramater called sort
@app.get('/blog')
def limitedblog(limit: int=10, published: bool=True,sort: Optional[str]=None):
    sort_info = sort if sort else "default sorting"
    return {'data': f'{limit} {"published" if published else "unpublished"} blog from db and sorted in {sort_info}'}


# @app.get('/about')
# def about():
#     return {'data':'about page'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

#here id is a path parameter
@app.get('/blog/{id}')
def show(id:int):
    #fetch blog with id = id
    return {'data':id} 

#python fastapi is intelligent enough to understand what comes from a path parameter (id) and what comes from query parameter(limit)
@app.get('/blog/{id}/comments')
def comments(id,limit=5):
    #fetch comments of blog with id = id
    return {'data':{'1','2',f'{limit}'}}

@app.get('/blog/{id}/comments')
def comments(id):
    #fetch comments of blog with id = id
    return {'data':{'1','2'}}
