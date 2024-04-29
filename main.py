from fastapi import FastAPI
from routers import client, branch, item, movement, user
from auth import authentication
from db import models
from db.database import engine


app = FastAPI()
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(movement.router)
app.include_router(item.router)
app.include_router(client.router)
app.include_router(branch.router)



@app.get('/')
def root():
    return "Hello World"

models.Base.metadata.create_all(engine)