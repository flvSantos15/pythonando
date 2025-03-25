from datetime import datetime

from ..model.entities.bancos import Bancos
from ..model.entities.contas import Conta
from ..model.entities.historico import Historico
from ..model.entities.status import Status
from ..model.entities.tipos_historico import Tipos
from ..views.conta import conta_controller


class UI:
  def start(self):
    while True:
      print('''
      [1] -> Criar conta
      [2] -> Desativar conta
      [3] -> Transferir saldo
      [4] -> Movimentar dinheiro
      [5] -> Total contas
      [6] -> Filtrar histórico
      ''')

      choice = int(input('Escolha uma opção: '))
      if choice == 1:
        self._create_account()
      elif choice == 2:
        self._deactivate_account()
      elif choice == 3:
        self._transfer_balance()
      elif choice == 4:
        self._moviment_balance()
      elif choice == 5:
        self._get_all_balances()
      elif choice == 6:
        self._filter_history_by_date()
      else:
        print('Opção inválida')
        break

  def _create_account(self):
    print('Digite o nome de algum dos bancos abaixo:')

    for banco in Bancos:
      print(f'======={banco.value}=======')

    banco = input("Digite o banco da conta: ").title()
    valor = float(input("Digite o valor em sua conta: "))
    
    conta = Conta(banco=Bancos(banco), valor=valor)

    conta_controller.create_account(conta)

  def _deactivate_account(self):
    print('Digite o id da conta que deseja desativar:')
    for conta in conta_controller.list_accounts():
      if conta.status == Status.ATIVO and conta.valor == 0:
        print(f'{conta.id} -> {conta.banco.value} -> R${conta.valor}')

    id_conta = int(input())

    try:
      conta_controller.deactivate_account(id_conta)
    except ValueError as e:
      print('Essa conta ainda tem saldo, faça uma movimentação para desativar')

  def _transfer_balance(self):
    print('Digite o id da conta de origem:')
    for conta in conta_controller.list_accounts():
      if conta.status == Status.ATIVO:
        print(f'{conta.id} -> {conta.banco.value} -> R${conta.valor}')

    id_origem = int(input())

    print('Digite o id da conta de destino:')
    for conta in conta_controller.list_accounts():
      if conta.status == Status.ATIVO:
        print(f'{conta.id} -> {conta.banco.value} -> R${conta.valor}')

    id_destino = int(input())

    valor = float(input('Digite o valor a ser transferido: '))

    conta_controller.transfer_balance(id_origem, id_destino, valor)

  def _moviment_balance(self):
    print('Digite o id da conta:')
    for conta in conta_controller.list_accounts():
      if conta.status == Status.ATIVO:
        print(f'{conta.id} -> {conta.banco.value} -> R${conta.valor}')

    id_conta = int(input())

    print('''
    [1] -> Entrada
    [2] -> Saida
    ''')

    choice = int(input('Escolha uma opção: '))
    if choice == 1:
      tipo = Tipos.ENTRADA
    else:
      tipo = Tipos.SAIDA

    valor = float(input('Digite o valor: '))

    historico = Historico(conta_id=id_conta, type=tipo, valor=valor)

    conta_controller.moviment_balance(historico)

  def _get_all_balances(self):
    for conta in conta_controller.list_accounts():
      print(f'{conta.id} -> {conta.banco.value} -> R${conta.valor}')

  def _filter_history_by_date(self):
    initial_date = input('Digite a data inicial: ')
    final_date = input('Digite a data final: ')

    initial_date = datetime.strptime(initial_date, '%Y-%m-%d').date()
    final_date = datetime.strptime(final_date, '%Y-%m-%d').date()

    for i in conta_controller.get_historic_by_date(initial_date, final_date):
      print(f'{i.valor} - {i.tipo.value}')

  def _create_graph_by_acount(self):
    return conta_controller.create_graph_by_acount()
  

