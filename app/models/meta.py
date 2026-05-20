from sqlalchemy import Column, Integer, Float, ForeignKey

from app.database import Base

class MetaFinanceira(Base):
    __tablename__ = "metas_financeiras"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    reserva_atual = Column(Float, default=0)

    reserva_meta = Column(Float, default=10000)