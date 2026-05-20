from pydantic import BaseModel

class SimulacaoSchema(BaseModel):
    tipo_calculo: str
    valor: float
    taxa: float
    tempo: int