from fastapi import FastAPI

from blog import schemas,models
from blog.database import engine

app = FastAPI()

#important step

models.Base.metadata.create_all(engine)


@app.post('/blog')
def create(request: schemas.Blog):
    return {f'title={request.title} and body={request.body}'}