from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth,vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

#models.Base.metadata.create_all(bind=engine) #Base engine for orm //from database.py file
#^
#|, dont need that anymore as we have alembic
app=FastAPI()

origins=['https://www.google.com','https://fastapi.tiangolo.com']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def message():
    return {"message":"Get check"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)