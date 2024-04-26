from fastapi import APIRouter, Depends
from routers.schemas import BranchBase, BranchDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_branch

router = APIRouter(
    prefix='/branch',
    tags=['branch']
)

@router.post('/', response_model=BranchDisplay)
def create_branch(request: BranchBase, db: Session = Depends(get_db)):
    return db_branch.create_branch(db, request)

@router.get('/')
def get_all(db: Session = Depends(get_db)):
    return db_branch.get_all(db)

@router.get('/{id}')
def get_client(id: int, db: Session = Depends(get_db)):
    return db_branch.get_branch(db, id)

