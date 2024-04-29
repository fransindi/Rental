from sqlalchemy.orm import Session
from routers.schemas import ItemBase
from db.models import DbItem
from fastapi import status, HTTPException

def create_item(db: Session, request: ItemBase):
    new_item = DbItem(
        name = request.name,
        kind = request.kind,
        size = request.size,
        gender = request.gender,
        available = True
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def get_item(db: Session, id: int):
    item = db.query(DbItem).filter(DbItem.id == id).first()
    if not item:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Item {item} already exists.')
    return item

def get_all(db: Session):
    return db.query(DbItem).all()

