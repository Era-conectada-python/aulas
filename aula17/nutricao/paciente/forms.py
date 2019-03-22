from django.forms import ModelForm

from paciente.models import Paciente, Dieta

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'idade', 'telefone', 'profissao', 'email']

class DietaForm(ModelForm):
    class Meta:
        model = Dieta
        fields = ['paciente', 'plano_alimentar', 'periodo']
