from sqlalchemy.orm import Session
from sqlalchemy import select
from routers.schemas import MovementBase
from db.models import DbMovement, DbPrice, DbItem, DbBranch, DbClient
from datetime import datetime, timedelta
from fastapi import HTTPException, status

def create_movement(db: Session, request: MovementBase):
    now = datetime.now()
    ends = now + timedelta(days=request.days) 
    price_days = db.query(DbPrice).count()
    if request.days > price_days:
        last_price = db.query(DbPrice).filter(DbPrice.days == price_days).first()
        price = (request.days - price_days) * 600 + last_price.price
    else:
        price = db.query(DbPrice).filter(DbPrice.days == request.days).first().price
    item_available = db.query(DbItem).filter(DbItem.id == request.item_id).first()
    if not item_available:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item dont founds')
    if item_available.available == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Item is not available.')
    branch = db.query(DbBranch).filter(DbBranch.id == request.branch_id).first()
    if not branch:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Branch dont found.')
    client = db.query(DbClient).filter(DbClient.id == request.client_id).first()
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Client dont found.')
    

    new_client = DbMovement(
        item_id = request.item_id,
        branch_id = request.branch_id,
        client_id = request.client_id,
        starts = now,
        ends = ends,
        price = price
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def get_movement(db: Session, id: int):
    client = db.query(DbMovement).filter(DbMovement.id == id).first()
    return client

def get_all(db: Session):
    return db.query(DbMovement).all()

def return_rental(db: Session, id: int):
    movement = get_movement(db, id)
    if datetime.now() > movement.ends:
        item = db.query(DbItem).filter(DbItem.id == movement.item_id).first()
        item.available == True
    return 'not so ok'