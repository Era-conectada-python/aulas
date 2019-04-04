from django import forms
from django.forms import ModelForm

from paciente.models import *

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'telefone', 'profissao', 'email', 'sexo']

class DietaForm(ModelForm):
    class Meta:
        model = Dieta
        fields = ['plano_alimentar', 'periodo']

class EspecialidadeForm(ModelForm):
    class Meta:
        model = Especialidade
        fields = ['nome', 'descricao']

class NutricionistaForm(ModelForm):
    class Meta:
        model = Nutricionista
        fields = ['nome', 'especialidades', 'email', 'telefone', 'crn']

class ConsultaForm(ModelForm):
    class Meta:
        model = Consulta
        fields = ['data_hora', 'tipo', 'local', 'dieta', 'paciente', 'nutricionista', 'avaliacao']

class AvaliacaoForm(ModelForm):
    class Meta:
        model = Avaliacao
        fields = ['peso', 'altura']
