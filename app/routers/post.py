from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas,oauth2
from typing import List, Optional
from ..database import get_db
from sqlalchemy.orm import Session

router= APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.get("/", response_model=list[schemas.Post] )
def get_posts(db: Session =Depends(get_db), current_user: int =Depends(oauth2.get_current_user), limit:int = 10,skip:int=0
              ,search: Optional[str]=""):
    print(limit)
    posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post) #Changed the path from "createposts" to "posts" cuz its the best practice
def create_post(post: schemas.PostCreate, db: Session =Depends(get_db), current_user: int =Depends(oauth2.get_current_user)):

    # print(current_user.id)
    # print(current_user.email)
    # print(current_user.password)
    new_post=models.Post(user_id=current_user.id,**post.dict()) #adding current_user.id to directly connect the user id with the post
    db.add(new_post)
    db.commit()
    db.refresh(new_post) #Just like RETURNING *   
    return new_post

@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session =Depends(get_db),current_user: int =Depends(oauth2.get_current_user)):
    posts=db.query(models.Post).filter(models.Post.id==id).first()
    print(posts)
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    return posts

@router.delete("/{id}")
def delete_post(id: int,db: Session =Depends(get_db), current_user: int =Depends(oauth2.get_current_user)):

    post_query=db.query(models.Post).filter(models.Post.id==id)

    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
    
    if post.user_id !=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    
    return {"message":"post deleted"}

@router.put("/{id}", response_model=schemas.Post)
def update_post(id:int,updated_post: schemas.PostCreate, db: Session =Depends(get_db), current_user: int =Depends(oauth2.get_current_user)):
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} not found")
    
    if post.user_id !=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
   
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()