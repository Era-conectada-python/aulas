from rest_framework import viewsets

from paciente.models import Paciente, Dieta
from nutricao.api.serializers import PacienteSerializer, DietaSerializer
from nutricao.api.filters import PacienteFilter


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    filter_class = PacienteFilter

class DietaViewSet(viewsets.ModelViewSet):
    queryset = Dieta.objects.all()
    serializer_class = DietaSerializer
