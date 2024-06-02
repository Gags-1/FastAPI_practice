from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, conint
from typing import Optional
#This is BaseModel used to set parameters in the posts that the user will create
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass
class UserReponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class config:
        orm_mode = True


#for reposne to user
class Post(PostBase):
    id: int
    created_at: datetime
    user_id: int
    user: UserReponse #This is used to add the user details in the post response\
    # vote: int
    #Rest of the parameters are same as PostBase
    class config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class config:
        orm_mode = True

class CreateUser(BaseModel):
    username: str
    email: EmailStr
    password: str



class UserLogin(BaseModel):
    email: EmailStr
    password: str   

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str]

class Vote(BaseModel):
    post_id: int
    dir: int = Field(..., ge=0, le=1)
