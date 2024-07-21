from core.authenticate.settings import pwd_context


def hash_password(plain_password: str):
    return pwd_context.hash(plain_password)