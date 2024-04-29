from sqlalchemy.orm import Session
from routers.schemas import ClientBase
from db.models import DbClient
from fastapi import HTTPException, status

def create_client(db: Session, request: ClientBase):
    client = db.query(DbClient).filter(DbClient.name == request.name).first()
    if not client:          
        new_client = DbClient(
            name = request.name,
            email = request.email
        )
        db.add(new_client)
        db.commit()
        db.refresh(new_client)
        return new_client
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Client {client} already exists.')

def get_client(db: Session, id: int):
    client = db.query(DbClient).filter(DbClient.id == id).first()
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Client not found.')
    return client

def get_all(db: Session):
    return db.query(DbClient).all()