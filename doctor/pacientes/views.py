from django.http import HttpResponse
from django.shortcuts import render


def pacientes(request):
  return render(request, 'pacientes.html')