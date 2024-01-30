# cuentas/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm 
from django.contrib import messages 
from django.urls import reverse
from . import models
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
#from django.views.generic import DateDetailView


def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, 'La cuenta se creó exitosamente')
            return redirect(reverse('home')) 
        else:
            messages.error(request, 'No se pudo crear la cuenta')  
            print(form.errors)
            return render(request, 'usuarios/crear.html', {'form': form}) 
    else:
        form = CustomUserCreationForm()

        return render(request, 'usuarios/crear.html', {'form': form})
    
def salir(request):
    logout(request)
    return redirect(reverse('home'))  

def ver(request, pk):
    user = get_object_or_404(models.CustomUser, pk=pk)
    return render(request, 'usuarios/ver.html', {'user': user})

def eliminar(request, pk):
    user = get_object_or_404(models.CustomUser, pk=pk)
    user.delete()
    return redirect(reverse('home'))

def editar(request, pk):
    user = get_object_or_404(models.CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect(reverse('home'))
        else:
            print(form.errors)
            return render(request, 'usuarios/editar.html', {'form': form})
    else:
        form = CustomUserCreationForm(instance=user)
        return render(request, 'usuarios/editar.html', {'form': form})


def entrar(request):
    if request.method == 'POST':
        
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse('home'))

    
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, 'usuarios/entrar.html')
    
    
    return render(request, 'usuarios/entrar.html')
