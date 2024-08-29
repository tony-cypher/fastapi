from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str


# Article in UserDisplay
class Article(BaseModel):
    title: str
    content: str
    published: bool
    class Config():
        from_attributes = True

class UserDisplay(BaseModel):
    username: str
    email: str
    items: list[Article] = []
    class Config():
        from_attributes = True


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


# User in ArticleDisplay
class User(BaseModel):
    id: int
    username: str

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config():
        from_attributes = True