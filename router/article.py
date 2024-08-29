from fastapi import APIRouter, Depends
from schema import ArticleBase, ArticleDisplay
from sqlalchemy.orm.session import Session
from db import db_article
from db.database import get_db

router = APIRouter(
    prefix='/article',
    tags=['article']
)

# create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session=Depends(get_db)):
    return db_article.create_article(db, request)

# get article
@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db: Session=Depends(get_db)):
    return db_article.get_article(db, id)