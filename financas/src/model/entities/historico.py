from datetime import date

from sqlmodel import Field, Relationship, SQLModel  # type: ignore

from .contas import Conta
from .tipos_historico import Tipos


class Historico(SQLModel, table=True):
  id: int = Field(primary_key=True)
  conta_id: int = Field(foreign_key="conta.id")
  conta: Conta = Relationship()
  type: Tipos = Field(default=Tipos.ENTRADA)
  valor: float
  data: date