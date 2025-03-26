from django.urls import path  # type: ignore

from . import views

urlpatterns = [
    path('test/', views.pacientes, name="pacientes"),
]
