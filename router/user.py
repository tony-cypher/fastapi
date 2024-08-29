from fastapi import APIRouter, Depends
from schema import UserBase, UserDisplay
from sqlalchemy.orm.session import Session
from db import db_user
from db.database import get_db

router = APIRouter(
    prefix='/user',
    tags=['user']
)

# create
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session=Depends(get_db)):
    return db_user.create_user(db, request)

# read

# update

# delete