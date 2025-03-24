from enum import Enum

from sqlmodel import Field, SQLModel  # type: ignore


class Bancos(Enum):
    NUBANK = "Nubank"
    ITAU = "Itau"
    SANTADER = "Santader"
    INTER = "Inter"

class Status(Enum):
   ATIVO = "Ativo"
   INATIVO = "Inativo"

class Conta(SQLModel, table=True):
  id: int = Field(primary_key=True)
  valor: float
  banco: Bancos = Field(default=Bancos.NUBANK)
  status: Status = Field(default=Status.ATIVO)

