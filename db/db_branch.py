from sqlalchemy.orm import Session
from routers.schemas import BranchBase
from db.models import DbBranch

def create_branch(db: Session, request: BranchBase):
    new_client = DbBranch(
        name = request.name,
        location = request.location
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def get_branch(db: Session, id: int):
    client = db.query(DbBranch).filter(DbBranch.id == id).first()
    return client

def get_all(db: Session):
    return db.query(DbBranch).all()