from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    def bcrypt(password: str):
        hashed_pwd = pwd_context.hash(password)
        return hashed_pwd
    
    def verify(hashed_pwd: str, pwd: str):
        return pwd_context.verify(pwd, hashed_pwd)