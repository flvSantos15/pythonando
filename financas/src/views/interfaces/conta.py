from abc import ABC, abstractmethod

from model.entities.contas import Conta


class ContaInterface(ABC):
  @abstractmethod
  def create_account(self, conta: Conta):
    pass
