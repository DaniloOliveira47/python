from pydantic import BaseModel, Field

class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str
    data_criacao: str
    data_conclusao: str | None = None
    concluida: bool = Field(default=False)
    usuario_id: int

