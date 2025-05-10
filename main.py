# import the FAST API
from fastapi import FastAPI

# create an instance of the FastAPI
app = FastAPI()

def index():
    return 'hello world'