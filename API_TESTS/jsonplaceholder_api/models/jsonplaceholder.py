from pydantic import BaseModel, EmailStr
from typing import Optional


class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class Comment(BaseModel):
    postId: int
    id: int
    name: str
    email: EmailStr
    body: str


class Update(BaseModel):
    userId: Optional[int] = None
    id: Optional[int] = None
    title: Optional[str] = None
    body: Optional[str] = None
