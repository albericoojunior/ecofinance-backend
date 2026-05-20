from fastapi import APIRouter

router = APIRouter(
    prefix="/carteira",
    tags=["Carteira"]
)

@router.get("/")
def listar_carteira():
    return {
        "acoes": [],
        "fiis": []
    }