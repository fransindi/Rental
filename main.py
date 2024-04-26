from fastapi import FastAPI
from routers import client, branch, item
from db import models
from db.database import engine

app = FastAPI()
app.include_router(client.router)
app.include_router(branch.router)
app.include_router(item.router)

@app.get('/')
def root():
    return "Hello World"

models.Base.metadata.create_all(engine)