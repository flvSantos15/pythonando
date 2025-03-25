from sqlmodel import SQLModel  # type: ignore
from src.model.configs.base import engine
from src.model.entities.bancos import Bancos
from src.model.entities.contas import Conta
from src.views.conta import conta_controller

# conta = Conta(
#   id=1,
#   valor=100,
#   banco=Bancos.NUBANK
# )

# conta_controller.create_account(conta)
conta_controller.list_accounts()

if __name__ == "__main__":
  SQLModel.metadata.create_all(engine)