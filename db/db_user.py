from sqlalchemy.orm import Session
from routers.schemas import UserBase
from db.models import DbUser
from fastapi import HTTPException, status
from .hash import Hash

def create_user(db: Session, request: UserBase):
    user = DbUser(
        username = request.username,
        email = request.email,
        branch_id = request.branch_id,
        password = Hash.bcrypt(request.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user
