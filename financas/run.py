from sqlmodel import SQLModel  # type: ignore
from src.model.configs.base import engine
from src.model.entities.contas import Conta

if __name__ == "__main__":
  SQLModel.metadata.create_all(engine)