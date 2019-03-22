from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import PacienteForm, DietaForm
from .models import Paciente

def paciente_view(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pacientes')

    else:
        form = PacienteForm()

    return render(request, 'template/paciente.html', {'form': form})


def dieta_view(request):
    pacientes = Paciente.objects.all()
    print(request.user)
    if request.method == 'POST':
        print('POST')
        form = DietaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dietas')

    else:
        form = DietaForm()

    return render(request, 'template/dieta.html', {'dieta': form, 'paciente': pacientes})