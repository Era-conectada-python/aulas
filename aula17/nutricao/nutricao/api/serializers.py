from rest_framework import serializers

from paciente.models import Paciente, Dieta


class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields = ('nome', 'idade', 'telefone', 'profissao', 'email')

class DietaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dieta
        fields = ('__all__')