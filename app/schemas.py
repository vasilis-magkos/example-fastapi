from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone_number: str


class User(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    phone_number: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: User


class PostOut(BaseModel):
    Post: Post
    Votes: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
