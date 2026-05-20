from pydantic import BaseModel

class MetaSchema(BaseModel):
    reserva_atual: float
    reserva_meta: float