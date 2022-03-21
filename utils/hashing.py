from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hashing:
    def create_hash(password: str) -> pwd_ctx:
        return pwd_ctx.hash(password)

    def verify_hash(hashed_password: str, plain_password: str) -> pwd_ctx:
        return pwd_ctx.verify(plain_password, hashed_password)

