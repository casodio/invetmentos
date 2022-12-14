from django.shortcuts import render, HttpResponse, redirect
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def investir(request):
    dados = {'dados':Investimento.objects.all()}

    return render(request, 'investimentos/investimentos.html', context=dados)

def detalhe(request, id):
    dados = {'dados':Investimento.objects.get(pk=id)}
    
    return render(request, 'investimentos/detalhes.html', dados)
@login_required
def criar(request):
    if request.method == 'POST':
        investform = InvestimentoForm(request.POST)
        if investform.is_valid():
            investform.save()
        return redirect('home')
    else:

        investform = InvestimentoForm()
        formulario = {"formulario" : investform}
        return render(request, 'investimentos/newinvest.html', context=formulario)
@login_required
def editarinvest(request, id):
    investimento = Investimento.objects.get(pk=id)
    if request.method == "GET":
        formulario = InvestimentoForm(instance=investimento)
        return render(request, 'investimentos/newinvest.html', {'formulario':formulario})

    else:
        formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('home')
@login_required
def excluinvest(request, id):
    investimento = Investimento.objects.get(pk=id)
    if request.method == 'POST':
        investimento.delete()
        return redirect('home')
    return render(request, 'investimentos/exclusao.html', {'item': investimento})

