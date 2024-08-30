from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm.session import Session
from db import db_user
from db.database import get_db
from typing import Optional
from datetime import datetime, timedelta, timezone
from jose import jwt
from jose.exceptions import JWTError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# openssl rand -hex 32      (generates a random 32bit secret key)
SECRET_KEY = 'a3617765afc927fa87aaf80c7933b178589a1aebd05efc9f81738212b1eb346c'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.now(timezone.utc) + expires_delta
  else:
    expire = datetime.now(timezone.utc) + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def get_current_user(token: str=Depends(oauth2_scheme), db: Session=Depends(get_db)):
    credentials_exception = HTTPException(
       status_code=status.HTTP_401_UNAUTHORIZED,
       detail='Could not validate credentials',
       headers={'WWW-Authenticate': "bearer"}
    )
    try:
       payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
       username: str=payload.get("sub")
       if username is None:
          raise credentials_exception
    except JWTError:
       raise credentials_exception
    
    user = db_user.get_user_by_username(db, username)
    if user is None:
       raise credentials_exception
    return user