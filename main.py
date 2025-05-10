# import the FAST API
from fastapi import FastAPI

# create an instance of the FastAPI
app = FastAPI()


# we are defining the path and get is called as operation and @app decorator is called as path operation decorator
@app.get('/')
#this function index is called as the path operation function

def index():
    return {'data':{'name':'Nithin'}}

@app.get('/about')
def about():
    return {'data':'about page'}