from django.shortcuts import redirect, render
from .models import * 
from django.views.generic import DetailView
from . import forms
from django.contrib import messages

# Create your views here.

class PersonajeDetailView(DetailView):
    model = Personaje
    template_name = 'historical/personaje_detail.html'
    context_object_name = 'personaje'
    
class HechoDetailView(DetailView):
    model = Hecho_Historico
    template_name = 'historical/hecho_detail.html'
    context_object_name = 'hecho'   


def hecho_historico(request):
    
    hechos = Hecho_Historico.objects.all()

    return render(request, 'historical/historical.html', {'hechos': hechos} )

def figuras(request):
    figuras = Personaje.objects.all()

    return render(request, 'historical/figuras.html', {'figuras': figuras} )


def buscar(request):
    buscar_query = request.GET.get('buscar')

    if buscar_query:
        hechos = Hecho_Historico.objects.filter(nombre__contains=buscar_query)
        figuras = Personaje.objects.filter(nombre__contains=buscar_query)

        if hechos or figuras:
            messages.success(request, f'Se encontraron resultados relacionados con "{buscar_query}"')
            return render(request, 'historical/busqueda_resultados.html', {'hechos': hechos, 'figuras': figuras})
        else:
            messages.warning(request, f'No se encontraron resultados relacionados con "{buscar_query}"')

    hechos = Hecho_Historico.objects.all()
    figuras = Personaje.objects.all()
    return render(request, 'historical/busqueda_resultados.html', {'hechos': hechos, 'figuras': figuras})


def alerta(request):
    if request.method == 'POST':
        form = forms.Alerta(request.POST)
        if form.is_valid():
            messages.success(request, 'Alerta enviada correctamente')
            return redirect('aviso')
            
   
    
    form = forms.Alerta()
    return render(request, 'historical/alerta.html', {'form': form})



