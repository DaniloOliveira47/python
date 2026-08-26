from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.banco.base import Base

class Tarefa(Base):
    __tablename__ = "tarefas"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    titulo: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    descricao: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="pendente"
    )

    usuario_id: Mapped[int] = mapped_column(
        nullable=False
    )