from sqlalchemy.orm import Session
from routers.schemas import ClientBase
from db.models import DbClient

def create_client(db: Session, request: ClientBase):
    new_client = DbClient(
        name = request.name,
        email = request.email
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def get_client(db: Session, id: int):
    client = db.query(DbClient).filter(DbClient.id == id).first()
    return client

def get_all(db: Session):
    return db.query(DbClient).all()