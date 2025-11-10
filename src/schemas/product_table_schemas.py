from typing import Optional
from pydantic import BaseModel


class InsertProductTable(BaseModel):
    cliente_id: int
    id_produto: int
    titulo: str
    imagem: str
    preco: str
    review: Optional[str] = None


class GetProductTable(BaseModel):
    cliente_id: int
