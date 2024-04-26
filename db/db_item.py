from sqlalchemy.orm import Session
from routers.schemas import ItemBase
from db.models import DbItem

def create_branch(db: Session, request: ItemBase):
    new_client = DbItem(
        name = request.name,
        kind = request.kind,
        size = request.size,
        gender = request.gender,
        available = True
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def get_branch(db: Session, id: int):
    client = db.query(DbItem).filter(DbItem.id == id).first()
    return client

def get_all(db: Session):
    return db.query(DbItem).all()

