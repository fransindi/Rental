from fastapi import APIRouter, Depends
from routers.schemas import MovementBase, UserAuth
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_movement
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix='/movement',
    tags=['movement']
)

@router.post('/')
def create_movement(request: MovementBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_movement.create_movement(db, request)

@router.get('/')
def get_all(db: Session = Depends(get_db)):
    return db_movement.get_all(db)

@router.get('/{id}')
def get_client(id: int, db: Session = Depends(get_db)):
    return db_movement.get_movement(db, id)

@router.post('/return/{id}')
def return_rental(id: int, db: Session = Depends(get_db)):
    return db_movement.return_rental(db, id)
