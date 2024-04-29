from pydantic import BaseModel

class ClientBase(BaseModel):
    name: str
    email: str

class ClientDisplay(ClientBase):
    id: int

class BranchBase(BaseModel):
    name: str
    location: str

class BranchDisplay(BranchBase):
    id: int

class ItemBase(BaseModel):
    name: str
    kind: str
    size: float
    gender: str


class MovementBase(BaseModel):
    item_id: int
    branch_id: int
    client_id: int
    days: int

class UserBase(BaseModel):
    username: str
    email: str
    branch_id: int
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    branch: BranchDisplay

class UserAuth(BaseModel):
    id: int
    username: str
    email: str