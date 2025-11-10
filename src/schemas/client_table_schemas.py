from pydantic import BaseModel, EmailStr


class InsertClientTable(BaseModel):
    nome: str
    email: EmailStr


class ReadClientTable(BaseModel):
    cliente_id: int


class UpdateClientTable(BaseModel):
    cliente_id: int
    nome: str
    email: EmailStr

class DeleteClientTable(BaseModel):
    cliente_id: int
