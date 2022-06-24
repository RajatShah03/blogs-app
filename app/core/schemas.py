from typing import List, Union
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

class Blog(BaseModel):
    title: str
    body: str

class BlogBase(Blog):
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[BlogBase] = []
    class Config():
        orm_mode = True

class ShowBlog(Blog):
    creator: ShowUser
    class Config():
        orm_mode = True

class Authentication(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
    