from sqlmodel import Field, SQLModel  # type: ignore
from src.model.entities.bancos import Bancos  # type: ignore
from src.model.entities.status import Status  # type: ignore


class Conta(SQLModel, table=True):
  id: int = Field(primary_key=True)
  valor: float
  banco: Bancos = Field(default=Bancos.NUBANK)
  status: Status = Field(default=Status.ATIVO)