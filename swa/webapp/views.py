from django.shortcuts import render
from django.contrib import messages
from .utils import *
from .models import *

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def administrator(request):
    return render(request, 'administracion/admin_general.html', getCountDatos())

def administrator_AgGrf(request):
    unis = Universidad.objects.all()
    if request.method == 'POST':
        temp_estadistica = Estadistica()
        temp_estadistica.anio_dato = request.POST.get('anio_input')
        if not Estadistica.objects.filter(anio_dato=temp_estadistica.anio_dato, tipoGrafico=temp_estadistica.tipoGrafico):
           temp_estadistica.tipoGrafico = request.POST.get('tipoGrafico_input')
           temp_estadistica.idUniversidad = request.POST.get('universidad_inpu')
           temp_estadistica.save()
           messages.success(request, 'Datos guardados correctamente')
        else:
            messages.error(request, 'Error al guardar los datos.')
        
    return render(request, 'administracion/CRUD_Grafico/Agregargrf.html', {'unis': unis})

def administrator_ModGrf(request):
    return render(request, 'administracion/CRUD_Grafico/Modificargrf.html')

def administrator_ElGrf(request):
    return render(request, 'administracion/CRUD_Grafico/Eliminargrf.html')

def administrator_AgUni(request):
    if request.method == 'POST':
        temp_uni = Universidad()
        temp_uni.nombreU = request.POST.get('nombreU_input')
        temp_uni.anio_periodo = request.POST.get('anio_periodo_input')
        if not Universidad.objects.filter(anio_periodo=temp_uni.anio_periodo, nombreU=temp_uni.nombreU):
            temp_uni.numInscritos = request.POST.get('inscritos_input')
            temp_uni.numGraduados = request.POST.get('graduados_input')
            temp_uni.numDesertados = request.POST.get('desertados_input')
            temp_uni.save()
            messages.success(request, 'Datos guardados correctamente.')
        else:
            messages.error(request, 'Error al guardar los datos.')
    return render(request, 'administracion/CRUD_Universidad/Agregaruni.html')

def administrator_ModUni(request):
    return render(request, 'administracion/CRUD_Universidad/Modificaruni.html')

def administrator_ElUni(request):
    return render(request, 'administracion/CRUD_Universidad/Eliminaruni.html')