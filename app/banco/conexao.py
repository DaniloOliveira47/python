from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.configuracao.configuracoes import configuracoes


motor = create_engine(
    configuracoes.DATABASE_URL,
    pool_pre_ping=True
)

SessaoBanco = sessionmaker(
    bind=motor,
    autoflush=False,
    autocommit=False
)


def obter_banco():
    banco = SessaoBanco()

    try:
        yield banco
    finally:
        banco.close()