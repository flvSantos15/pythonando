from typing import Optional

from ninja import ModelSchema, Schema  # type: ignore

from .models import Alunos


class AlunosSchema(ModelSchema):
    class Meta:
        model = Alunos
        fields = ['nome', 'email', 'faixa', 'data_nascimento']


class ProgressoAlunoSchema(Schema):
    email: str
    nome: str
    faixa: str
    total_aulas: int
    aulas_necessarias_para_proxima_faixa: int


class AulasRealizadasSchema(Schema):
    qtd: Optional[int] = 1
    email_aluno: str
