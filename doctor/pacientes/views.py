from django.contrib import messages  # type: ignore
from django.contrib.messages import constants  # type: ignore
from django.shortcuts import redirect, render  # type: ignore

from .models import Consultas, Pacientes, Tarefas

# Parei em 3:16:30

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
    tarefas = Tarefas.objects.all()
    consultas = Consultas.objects.filter(paciente=paciente).order_by('-data')
    return render(request, 'paciente.html', {'paciente': paciente, 'tarefas': tarefas, 'consultas': consultas})
  elif request.method == "POST":
    humor = request.POST.get('humor')
    registro_geral = request.POST.get('registro_geral')
    video = request.FILES.get('video')
    tarefas = request.POST.getlist('tarefas')

    consulta = Consultas(
      humor=int(humor),
      registro_geral=registro_geral,
      video=video,
      paciente=paciente
    )
    consulta.save()
    for tarefa in tarefas:
      tarefa = Tarefas.objects.get(id=tarefa)
      paciente.tarefas.add(tarefa)

    consulta.save()

    messages.add_message(request, constants.SUCCESS, 'Consulta adicionada com sucesso')
    return redirect('/pacientes/{id}')

def atualizar_paciente(request, id):
  paciente = Pacientes.objects.get(id=id)
  pagamento_em_dia = request.POST.get('pagamento_em_dia')
  status = True if pagamento_em_dia == 'ativo' else False
  paciente.pagamento_em_dia = status
  paciente.save()
  return redirect(f'/pacientes/{id}')

def excluir_consulta(request, id):
  consulta = Consultas.objects.get(id=id)
  consulta.delete()
  return redirect(f'/pacientes/{consulta.paciente.id}')

def consulta_publica(request, id):
    consulta = Consultas.objects.get(id=id)
    if not consulta.paciente.pagamento_em_dia:
        raise Http404()

    return render(request, 'consulta_publica.html', {'consulta': consulta})

