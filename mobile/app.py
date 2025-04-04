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

    def criar_aluno():
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

    students_table = ft.DataTable(
        columns=[
            ft.DataColumn("Nome"),
            ft.DataColumn("Email"),
            ft.DataColumn("Faixa"),
            ft.DataColumn("Data de Nascimento"),
        ],
        rows=[],
    )

    def list_students(e):
        response = requests.get(f"{API_BASE_URL}/alunos/")
        if response.status_code == 200:
            alunos = response.json()
            students_table.rows.clear()
            
            students_table.rows = [
                ft.DataRow(cells=[
                    ft.DataCell(aluno["nome"]),
                    ft.DataCell(aluno["email"]),
                    ft.DataCell(aluno["faixa"]),
                    ft.DataCell(aluno["data_nascimento"]),
                ]) for aluno in alunos
            ]
            list_result.value = f"{len(alunos)} alunos encontrados"
        else:
            list_result.value = f"Erro: {response.text}"

        page.update()
    
    list_result = ft.Text()
    list_button = ft.ElevatedButton("Listar Alunos", on_click=list_students)
    list_students_tab = ft.Column([ list_button, list_result, students_table ], scroll=True)

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
          ft.Tab(text="Criar Aluno", content=criar_aluno_tab),
          ft.Tab(text="Listar Alunos", content=list_students_tab),
        ]
    )

    page.add(tabs)

if __name__ == "__main__":
    ft.app(target=main)
