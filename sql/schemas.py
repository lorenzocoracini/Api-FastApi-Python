from typing import Union

from pydantic import BaseModel


class IngressoBase(BaseModel):
    title: str
    description: Union[str, None] = None


class IngressoCreate(IngressoBase):
    pass


class Ingresso(IngressoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class CompradorBase(BaseModel):
    email: str


class CompradorCreate(CompradorBase):
    password: str


class Comprador(CompradorBase):
    id: int
    is_active: bool
    items: list[Ingresso] = []

    class Config:
        orm_mode = True
