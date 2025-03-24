from sqlmodel import SQLModel, create_engine  # type: ignore
from src.model.entities.contas import Conta

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

if __name__ == "__main__":
  SQLModel.metadata.create_all(engine)