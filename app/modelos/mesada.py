from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.banco.base import Base

class Mesada(Base):
    __tablename__ = "mesadas"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    valor: Mapped[float] = mapped_column(
        nullable=False
    )

    data_pagamento: Mapped[str] = mapped_column(
        String(10),
        nullable=False
    )

    usuario_id: Mapped[int] = mapped_column(
        nullable=False
    )