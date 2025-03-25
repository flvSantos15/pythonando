from sqlmodel import SQLModel  # type: ignore
from src.model.configs.base import engine
from src.templates.contas import UI

ui = UI()
ui.start()

if __name__ == "__main__":
  SQLModel.metadata.create_all(engine)