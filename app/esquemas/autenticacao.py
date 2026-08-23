from pydantic import BaseModel, EmailStr


class CadastroUsuario(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    tipo: str