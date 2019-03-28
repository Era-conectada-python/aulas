from rest_framework import serializers

from paciente.models import Paciente, Dieta


class DietaSerializer(serializers.ModelSerializer):
    paciente = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Dieta
        fields = ('paciente', 'plano_alimentar', 'periodo', 'paciente')

class PacienteSerializer(serializers.ModelSerializer):
    dieta = DietaSerializer(many=True, read_only=True)
    class Meta:
        model = Paciente
        fields = ('nome', 'idade', 'telefone', 'profissao', 'email', 'dieta')
