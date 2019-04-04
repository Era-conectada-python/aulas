from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import *
from .models import *

def paciente_view(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pacientes')

    else:
        form = PacienteForm()

    return render(request, 'template/form.html', {'form': form})


def dieta_view(request):
    if request.method == 'POST':
        form = DietaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dietas')

    else:
        form = DietaForm()

    return render(request, 'template/form.html', {'form': form})

def especialidade_view(request):
    if request.method == 'POST':
        form = EspecialidadeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/especialidades')

    else:
        form = EspecialidadeForm()

    return render(request, 'template/form.html', {'form': form})

def nutricionista_view(request):
    if request.method == 'POST':
        form = NutricionistaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/nutricionistas')

    else:
        form = NutricionistaForm()

    return render(request, 'template/form.html', {'form': form})

def consulta_view(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/consultas')

    else:
        form = ConsultaForm()

    return render(request, 'template/form.html', {'form': form})

def avaliacao_view(request):
    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/avaliacoes')

    else:
        form = AvaliacaoForm()

    return render(request, 'template/form.html', {'form': form})