from fastapi import APIRouter, Depends
from schema import ArticleBase, ArticleDisplay, UserBase
from sqlalchemy.orm.session import Session
from db import db_article
from db.database import get_db
from auth.oauth2 import oauth2_scheme, get_current_user

router = APIRouter(
    prefix='/article',
    tags=['article']
)

# create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session=Depends(get_db), current_user: UserBase=Depends(get_current_user)):
    return db_article.create_article(db, request)

# get article
@router.get('/{id}')
def get_article(id: int, db: Session=Depends(get_db), current_user: UserBase=Depends(get_current_user)):
    return {
        'data': db_article.get_article(db, id),
        'current_user': current_user
    }