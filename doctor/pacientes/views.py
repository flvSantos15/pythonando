from django.contrib import messages  # type: ignore
from django.contrib.messages import constants  # type: ignore
from django.shortcuts import redirect, render  # type: ignore

from .models import Pacientes


def pacientes(request):
  if request.method == "GET":
    queixas = Pacientes.queixa_choices
    pacientes = Pacientes.objects.all()
    return render(request, 'pacientes.html', {'queixas': queixas, 'pacientes': pacientes})
  elif request.method == "POST":
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    telefone = request.POST.get('telefone')
    queixa = request.POST.get('queixa')
    foto = request.FILES.get('foto')

    if len(nome.strip()) == 0 or not foto:
        messages.add_message(request, constants.ERROR, 'O campo nome e foto são obrigatórios')
        return redirect('pacientes')

    paciente = Pacientes(
        nome=nome,
        email=email,
        telefone=telefone,
        queixa=queixa,
        foto=foto
    )
    paciente.save()

    messages.add_message(request, constants.SUCCESS, 'Paciente adicionado com sucesso')
    return redirect('pacientes')
  

def paciente_view(request, id):
  paciente = Pacientes.objects.get(id=id)
  if request.method == "GET":
    return render(request, 'paciente.html', {'paciente': paciente})

def atualizar_paciente(request, id):
  paciente = Pacientes.objects.get(id=id)
  pagamento_em_dia = request.POST.get('pagamento_em_dia')
  status = True if pagamento_em_dia == 'ativo' else False
  paciente.pagamento_em_dia = status
  paciente.save()
  return redirect(f'/pacientes/{id}')
