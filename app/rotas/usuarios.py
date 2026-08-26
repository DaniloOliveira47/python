from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.banco.conexao import obter_banco
from app.esquemas.mesada import Mesada as MesadaSchema
from app.modelos.mesada import Mesada as MesadaModel

router = APIRouter(
    prefix="/mesadas",
    tags=["Mesadas"]
)

@router.post("/")
def criar_mesada(
    mesada: MesadaSchema,
    banco: Session = Depends(obter_banco)
):
    nova_mesada = MesadaModel(
        valor=mesada.valor,
        data_pagamento=mesada.data_pagamento,
        usuario_id=mesada.usuario_id
    )
    banco.add(nova_mesada)
    banco.commit()
    banco.refresh(nova_mesada)
    return nova_mesada