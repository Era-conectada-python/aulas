from rest_framework import viewsets

from paciente.models import Paciente, Dieta
from nutricao.api.serializers import *
from nutricao.api.filters import PacienteFilter


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_class = PacienteFilter

class DietaViewSet(viewsets.ModelViewSet):
    queryset = Dieta.objects.all()
    serializer_class = DietaSerializer

class PacienteDietasViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteDietasSerializer

class DietaPacientesViewSet(viewsets.ModelViewSet):
    queryset = Dieta.objects.all()
    serializer_class = DietaPacientesSerializer


