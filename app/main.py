from fastapi import FastAPI
from pydantic import BaseModel
from . import models
from .database import engine
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine) #Base enhine for orm //from database.py file

app=FastAPI()

@app.get("/")
def message():
    return {"message":"Get check"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)