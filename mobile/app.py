import flet as ft
import requests

# URL base da API – ajuste conforme necessário
API_BASE_URL = "http://localhost:8000/api"

# Parei em 43:22

def main(page: ft.Page):
    page.title = "Exemplo"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    nome_field = ft.TextField(label="Nome")
    email_field = ft.TextField(label="Email")
    faixa_field = ft.TextField(label="Faixa")
    data_nascimento_field = ft.TextField(label="Data de Nascimento (YYYY-MM-DD)")

    def criar_aluno(e):
        payload = {
            "nome": nome_field.value,
            "email": email_field.value,
            "faixa": faixa_field.value,
            "data_nascimento": data_nascimento_field.value,
        }

        response = requests.post(f"{API_BASE_URL}/", json=payload)
        if response.status_code == 201:
            aluno = response.json()
            create_result.value = f'Aluno criado: {aluno}'
        else:
            create_result.value = f"Erro: {response.text}"

        page.update()

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
