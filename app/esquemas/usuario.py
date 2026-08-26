from pydantic import BaseModel, EmailStr    

class Usuario(BaseModel):
    id: int
    nome: str
    email: EmailStr
    tipo: str
    id_familia: int

