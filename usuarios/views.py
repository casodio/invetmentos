from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from usuarios.templates.usuarios.forms import UserRegisterForm

# Create your views here.
def usuarionovo(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'Usuario {usuario} registrado com sucesso!')
            return redirect('login')

    else:
        formulario = UserRegisterForm()

    return render(request, 'usuarios/registrar.html', {'formulario':formulario})

def acesso(request):
    
    return render(request, 'usuarios/semacesso.html')

