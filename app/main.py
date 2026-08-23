from fastapi import FastAPI

from app.banco.base import Base
from app.banco.conexao import motor
from app.modelos.usuario import Usuario
from app.rotas.autenticacao import router as rota_autenticacao


Base.metadata.create_all(bind=motor)


app = FastAPI(
    title="Família+ API",
    description="API para gerenciamento de tarefas e mesadas familiares",
    version="1.0.0"
)


app.include_router(rota_autenticacao)


@app.get("/")
def inicio():
    return {
        "mensagem": "Família+ API funcionando!"
    }