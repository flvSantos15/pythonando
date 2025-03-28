from django.urls import path  # type: ignore

from . import views

urlpatterns = [
    path('', views.pacientes, name="pacientes"),
    path('<int:id>', views.paciente_view, name="paciente_view"),
    path('atualizar_paciente/<int:id>', views.atualizar_paciente, name="atualizar_paciente"),
]
