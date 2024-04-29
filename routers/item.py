from fastapi import APIRouter, Depends
from routers.schemas import ItemBase
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_item

router = APIRouter(
    prefix='/item',
    tags=['item']
)

@router.post('/')
def create_item(request: ItemBase, db: Session = Depends(get_db)):
    return db_item.create_item(db, request)

@router.get('/')
def get_all(db: Session = Depends(get_db)):
    return db_item.get_all(db)

@router.get('/{id}')
def get_item(id: int, db: Session = Depends(get_db)):
    return db_item.get_item(db, id)

