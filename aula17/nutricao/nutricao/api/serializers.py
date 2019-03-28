from rest_framework import serializers

from paciente.models import Paciente, Dieta


class DietaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dieta
        fields = ('plano_alimentar', 'periodo')

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('nome', 'idade', 'telefone', 'profissao', 'email')

class DietaPacientesSerializer(serializers.ModelSerializer):
    paciente = PacienteSerializer(many=True, read_only=True)
    class Meta:
        model = Dieta
        fields = ('paciente', 'plano_alimentar', 'periodo')

class PacienteDietasSerializer(serializers.ModelSerializer):
    dieta = DietaSerializer(many=True, read_only=True)
    class Meta:
        model = Paciente
        fields = ('nome', 'idade', 'telefone', 'profissao', 'email', 'dieta')
