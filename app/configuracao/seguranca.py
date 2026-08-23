from passlib.context import CryptContext


criptografia = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def criptografar_senha(senha: str) -> str:
    return criptografia.hash(senha)


def verificar_senha(senha: str, senha_criptografada: str) -> bool:
    return criptografia.verify(
        senha,
        senha_criptografada
    )