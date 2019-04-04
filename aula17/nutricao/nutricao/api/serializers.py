from rest_framework import serializers

from paciente.models import *


class DietaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dieta
        fields = ('plano_alimentar', 'periodo')

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('nome', 'data_nascimento', 'telefone', 'profissao', 'email')

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = ('nome', 'descricao')

class NutricionistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutricionista
        fields = ('nome', 'especialidades', 'email', 'telefone', 'crn')

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ('data_hora', 'tipo', 'local', 'dieta', 'paciente', 'nutricionista')

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('peso', 'altura', 'consulta')
