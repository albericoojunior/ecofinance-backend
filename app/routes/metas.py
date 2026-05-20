from fastapi import APIRouter

router = APIRouter(
    prefix="/metas",
    tags=["Metas"]
)

@router.get("/")
def listar_metas():
    return {
        "message": "Metas funcionando"
    }