from sqlalchemy.orm import Session
from routers.schemas import BranchBase
from db.models import DbBranch
from fastapi import HTTPException, status


def create_branch(db: Session, request: BranchBase):
    branch = db.query(DbBranch).filter(DbBranch.name == request.name).first()
    if not branch:    
        new_branch = DbBranch(
            name = request.name,
            location = request.location
        )
        db.add(new_branch)
        db.commit()
        db.refresh(new_branch)
        return new_branch
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'Branch {branch} already exists.')

def get_branch(db: Session, id: int):
    branch = db.query(DbBranch).filter(DbBranch.id == id).first()
    if not branch:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Client not found.')
    return branch

def get_all(db: Session):
    return db.query(DbBranch).all()