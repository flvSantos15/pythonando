from datetime import date

from sqlmodel import Session, select  # type: ignore

from ....model.configs.base import engine
from ....model.entities.bancos import Bancos
from ....model.entities.contas import Conta
from ....model.entities.historico import Historico
from ....model.entities.status import Status
from ....model.entities.tipos_historico import Tipos


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

def list_accounts():
  with Session(engine) as session:
    statement = select(Conta)
    results = session.exec(statement).all()
  return results

def deactivate_account(id: int):
  with Session(engine) as session:
    statement = select(Conta).where(Conta.id == id)
    conta = session.exec(statement).first()

    if not conta:
      print("Não existe uma conta com esse id cadastrado")
      return
    
    if conta.valor > 0:
      raise ValueError("Não é possível desativar uma conta com saldo maior que zero")

    conta.status = Status.INATIVO
    session.commit()
    return
  
def transfer_balance(id_origem: int, id_destino: int, valor: float):
  with Session(engine) as session:
    statement = select(Conta).where(Conta.id == id_origem)
    conta_origem = session.exec(statement).first()

    if not conta_origem:
      raise ValueError("Não existe uma conta com esse id cadastrado")

    statement = select(Conta).where(Conta.id == id_destino)
    conta_destino = session.exec(statement).first()

    if not conta_destino:
      raise ValueError("Não existe uma conta com esse id cadastrado")

    if conta_origem.status != Status.ATIVO:
      raise ValueError("A conta de origem está inativa")
    
    if conta_destino.status != Status.ATIVO:
      raise ValueError("A conta de destino está inativa")

    if conta_origem.valor < valor:
      raise ValueError("Saldo insuficiente")

    conta_origem.valor -= valor # Retira o valor da conta de origem
    conta_destino.valor += valor # Adiciona o valor na conta de destino
    session.commit()

def moviment_balance(historico: Historico):
  with Session(engine) as session:
    statement = select(Conta).where(Conta.id == historico.conta_id)
    conta = session.exec(statement).first()

    if not conta:
      raise ValueError("Não existe uma conta com esse id cadastrado")

    if conta.status != Status.ATIVO:
      raise ValueError("A conta está inativa")

    if historico.tipo < Tipos.ENTRADA:
      conta.valor += historico.valor
    else:
      if conta.valor < historico.valor:
        raise ValueError("Saldo insuficiente")
      conta.valor -= historico.valor

    session.add(historico)
    session.commit()
    return historico

def get_all_balances():
  with Session(engine) as session:
    statement = select(Conta)
    contas = session.exec(statement).all()

    total_balance = 0
    for conta in contas:
      total_balance += conta.valor

  return total_balance


conta = Conta(
  id=1,
  valor=100,
  banco=Bancos.NUBANK
)

create_account(conta)