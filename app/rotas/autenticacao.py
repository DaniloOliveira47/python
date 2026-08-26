from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.banco.conexao import obter_banco
from app.esquemas.autenticacao import CadastroUsuario


router = APIRouter(
    prefix="/autenticacao",
    tags=["Autenticação"]
)


@router.post("/cadastro")

def cadastrar_usuario(
    dados: CadastroUsuario,
    banco: Session = Depends(obter_banco)
):
    return {
        "mensagem": "Cadastro recebido!",
        "nome": dados.nome,
        "email": dados.email,
        "tipo": dados.tipo
    }