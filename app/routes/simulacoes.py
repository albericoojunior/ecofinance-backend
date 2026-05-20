from fastapi import APIRouter

from app.schemas.simulacao import (
    SimulacaoSchema
)

from app.services.calculos import (
    calcular_juros_compostos
)

router = APIRouter(
    prefix="/simulacoes",
    tags=["Simulações"]
)

@router.post("/")
def simular(
    data: SimulacaoSchema
):

    resultado = calcular_juros_compostos(
        data.valor,
        data.taxa,
        data.tempo
    )

    return resultado