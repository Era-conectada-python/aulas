"""nutricao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path

from nutricao.api.views import *
from paciente import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'pacientes', PacienteViewSet, basename='pacientes')
router.register(r'dietas', DietaViewSet, basename='dietas')
router.register(r'especialidades', EspecialidadeViewSet, basename='especialidades')
router.register(r'nutricionistas', NutricionistaViewSet, basename='nutricionistas')
router.register(r'consultas', ConsultaViewSet, basename='consultas')
router.register(r'avaliacoes', AvaliacaoViewSet, basename='avaliacoes')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('form-paciente/', views.paciente_view),
    path('form-dieta/', views.dieta_view),
    path('form-especialidade/', views.especialidade_view),
    path('form-nutricionista/', views.nutricionista_view),
    path('form-consulta/', views.consulta_view),
    path('form-avaliacao/', views.avaliacao_view)
]