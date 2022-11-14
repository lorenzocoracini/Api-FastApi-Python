from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import database


class Comprador(database.Base):
    __tablename__ = "compradores"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    ingressos = relationship("Ingresso", back_populates="owner")


class Ingresso(database.Base):
    __tablename__ = "ingressos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("compradores.id"))

    owner = relationship("Comprador", back_populates="ingressos")
