import flet as ft
import requests

# URL base da API – ajuste conforme necessário
API_BASE_URL = "http://localhost:8000/api"

# Parei em 2:09:41

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

    student_email_field = ft.TextField(label="Email do Aluno")
    qtd_field = ft.TextField(label="Quantidade de aulas", value="1")
    aula_result = ft.Text()

    def marcar_aula_click(e):
        payload = {
            "email_aluno": student_email_field.value,
            "qtd": int(qtd_field.value),
        }

        response = requests.post(f"{API_BASE_URL}/aula_realizada/", json=payload)
        if response.status_code == 200:
            aula_result.value = f"Sucesso: {response.json()}"
        else:
            aula_result.value = f"Erro: {response.text}"
        page.update()

    email_progress_field = ft.TextField(label="Email do Aluno")
    progress_result = ft.Text()

    def consultar_progresso_click(e):
        email = email_progress_field.value
        response = requests.get(f"{API_BASE_URL}/progresso_aluno/", params={'email_aluno': email})

        if response.status_code == 200:
            progress = response.json()
            progress_result.value = (
                f"Nome: {progress.get('nome')}\n"
                f"Email: {progress.get('email')}\n"
                f"Faixa: {progress.get('faixa')}\n"
                f"Total de aulas concluidas: {progress.get('total_aulas')}\n"
                f"Aulas necessarias para a proxima faixa: {progress.get('aulas_necessarias_para_proxima_faixa')}"
            )
        else:
            progress_result.value = f"Erro: {response.text}"
        page.update()

    progress_button = ft.ElevatedButton("Consultar progresso", on_click=consultar_progresso_click)
    progress_tab = ft.Column([ email_progress_field, progress_button, progress_result], scroll=True)

    aula_button = ft.ElevatedButton("Realizar Aula", on_click=marcar_aula_click)
    aula_tab = ft.Column([ student_email_field, qtd_field, aula_button, aula_result], scroll=True)

    tabs = ft.Tabs(
        selected_index=0,
        tabs=[
          ft.Tab(text="Criar Aluno", content=criar_aluno_tab),
          ft.Tab(text="Listar Alunos", content=list_students_tab),
          ft.Tab(text="Cadastrar Aula", content=aula_tab),
          ft.Tab(text="Progresso do aluno", content=progress_tab),
        ]
    )

    page.add(tabs)

if __name__ == "__main__":
    ft.app(target=main)
