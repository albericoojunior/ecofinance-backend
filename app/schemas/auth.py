from pydantic import BaseModel, EmailStr

class RegisterSchema(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    senha: str

class LoginSchema(BaseModel):
    email: EmailStr
    senha: str