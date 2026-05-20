from sqlalchemy import Column, Integer, Float, String, ForeignKey

from app.database import Base

class Carteira(Base):
    __tablename__ = "carteira"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    ticker = Column(String)

    tipo = Column(String)

    quantidade = Column(Float)

    preco_medio = Column(Float)