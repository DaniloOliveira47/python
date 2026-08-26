from pydantic import BaseModel, EmailStr

class Mesada(BaseModel):
    id: int
    valor: float
    data_pagamento: str
    usuario_id: int