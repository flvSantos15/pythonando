from django.db import models  # type: ignore


# Create your models here.
class Alunos(models.Model):
  faixas_choices = (
    ('B', 'Branca'),
    ('A', 'Azul'),
    ('R', 'Roxa'),
    ('M', 'Marrom'),
    ('P', 'Preta'),
  )
  nome = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  data_nascimento = models.DateField(null=True, blank=True)
  faixa = models.CharField(max_length=1, choices=faixas_choices, default='B')

  def __str__(self):
    return self.nome
  

class AulasConcluidas(models.Model):
    faixas_choices = (
      ('B', 'Branca'),
      ('A', 'Azul'),
      ('R', 'Roxa'),
      ('M', 'Marrom'),
      ('P', 'Preta'),
    )
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    faixa_atual = models.CharField(max_length=1, choices=faixas_choices)

    def __str__(self):
        return self.aluno.nome


