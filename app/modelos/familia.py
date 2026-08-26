from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.banco.base import Base

class Familia(Base):
    __tablename__ = "familias"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    descricao: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )
    