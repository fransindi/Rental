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

