from sqlmodel import Session, select  # type: ignore
from src.model.configs.base import engine
from src.model.entities.contas import Conta

#  Parei em 1:00:06

def create_account(conta: Conta):
  with Session(engine) as session:
    statement = select(Conta).where(Conta.banco == conta.banco)
    results = session.exec(statement).all()

    if results:
      print("Já existe uma conta com esse banco cadastrado")
      return

    session.add(conta) # Adiciona no banco
    session.commit() # Salva no banco
    return conta
