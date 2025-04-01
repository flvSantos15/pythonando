import flet as ft
import requests

# URL base da API – ajuste conforme necessário
API_BASE_URL = "http://localhost:8000/api/treino"

# Parei em 30:10

def main(page: ft.Page):
    page.title = "Exemplo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    nome_field = ft.TextField(label="Nome")
    email_field = ft.TextField(label="Email")
    faixa_field = ft.TextField(label="Faixa")
    data_nascimento_field = ft.TextField(label="Data de Nascimento (YYYY-MM-DD)")

    def criar_aluno(e):
        print("Criando aluno...")

    create_result = ft.Text()
    create_button = ft.ElevatedButton("Criar Aluno", on_click=criar_aluno)

    criar_aluno_tab = ft.Column(
        [
            nome_field,
            email_field,
            faixa_field,
            data_nascimento_field,
            create_button,
            create_result,
        ],
        scroll=True
    )

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
          ft.Tab(text="Criar Aluno", content=criar_aluno_tab),
        ]
    )

    page.add(tabs)

if __name__ == "__main__":
    ft.app(target=main)
