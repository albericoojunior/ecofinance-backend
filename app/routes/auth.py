from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user import User

from app.schemas.auth import (
    RegisterSchema,
    LoginSchema
)

from app.security import (
    gerar_hash,
    verificar_senha,
    criar_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
def register(
    data: RegisterSchema,
    db: Session = Depends(get_db)
):

    usuario = db.query(User).filter(
        User.email == data.email
    ).first()

    if usuario:
        raise HTTPException(
            status_code=400,
            detail="Email já cadastrado"
        )

    novo_usuario = User(
        nome=data.nome,
        cpf=data.cpf,
        email=data.email,
        senha=gerar_hash(data.senha)
    )

    db.add(novo_usuario)

    db.commit()

    db.refresh(novo_usuario)

    return {
        "message": "Usuário criado"
    }

@router.post("/login")
def login(
    data: LoginSchema,
    db: Session = Depends(get_db)
):

    usuario = db.query(User).filter(
        User.email == data.email
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="Credenciais inválidas"
        )

    senha_valida = verificar_senha(
        data.senha,
        usuario.senha
    )

    if not senha_valida:
        raise HTTPException(
            status_code=401,
            detail="Credenciais inválidas"
        )

    token = criar_token({
        "sub": str(usuario.id)
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }