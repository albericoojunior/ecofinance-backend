from sqlalchemy import Column, Integer, Float, String, ForeignKey

from app.database import Base

class Simulacao(Base):
    __tablename__ = "simulacoes"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    tipo_calculo = Column(String)

    valor = Column(Float)

    taxa = Column(Float)

    tempo = Column(Integer)

    resultado = Column(Float)