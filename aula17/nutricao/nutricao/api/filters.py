import django_filters

from paciente.models import Paciente


class PacienteFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Paciente
        fields = ['nome']