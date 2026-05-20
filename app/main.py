from fastapi import FastAPI

from app.database import (
    Base,
    engine
)

from app.routes.auth import (
    router as auth_router
)

from app.routes.metas import (
    router as metas_router
)

from app.routes.simulacoes import (
    router as simulacoes_router
)

from app.routes.carteira import (
    router as carteira_router
)

Base.metadata.create_all(
    bind=engine
)

app = FastAPI(
    title="EcoFinance API"
)

app.include_router(auth_router)

app.include_router(metas_router)

app.include_router(simulacoes_router)

app.include_router(carteira_router)

@app.get("/")
def home():
    return {
        "message": "EcoFinance API Online"
    }