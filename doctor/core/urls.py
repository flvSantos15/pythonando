"""
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin  # type: ignore
from django.urls import include, path  # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('pacientes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
