from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from .utils import *
from .models import *

# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def administrator(request):
    return render(request, 'administracion/admin_general.html', getCountDatos())

def administrator_AgGrf(request):
    unis = Universidad.objects.all()
    if request.method == 'POST' and request.POST.get('form_id') == 'form_AgregarGrf':
        temp_estadistica = Estadistica()
        temp_1 = request.POST.get('anio_input')
        temp_2 = request.POST.get('tipoGrafico_input')
        temp_3 = int(request.POST.get('universidad_input'))
        if not Estadistica.objects.filter(anio_dato=temp_1, tipoGrafico=temp_2, idUniversidad_id=temp_3):
            temp_estadistica.anio_dato = temp_1
            temp_estadistica.tipoGrafico = temp_2
            temp_estadistica.idUniversidad_id = temp_3
            temp_estadistica.idAdmin_id = 1
            temp_estadistica.save()
            messages.success(request, 'Datos guardados correctamente')
        else:
            messages.error(request, 'Error al guardar los datos. No puedes ingresar un grafico que ya ha sido ingresado')
        
    return render(request, 'administracion/CRUD_Grafico/Agregargrf.html', {'unis': unis})

def administrator_ModGrf(request):
    return render(request, 'administracion/CRUD_Grafico/Modificargrf.html')

def administrator_ElGrf(request):
    return render(request, 'administracion/CRUD_Grafico/Eliminargrf.html')

def administrator_AgUni(request):
    if request.method == 'POST' and request.POST.get('form_id') == 'form_AgregarUni':
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
            messages.error(request, 'Error al guardar los datos, Ya hay datos existentes')
    return render(request, 'administracion/CRUD_Universidad/Agregaruni.html')

def administrator_ModUni(request):
    unis2 = Universidad.objects.all()
    if 'form_activado' in request.COOKIES:
        form_activado = request.COOKIES['form_activado']
    else:
        form_activado = False
    form_modificar = UniversidadForm(initial={})
    response =  render(request, 'administracion/CRUD_Universidad/Modificaruni.html', {'unis': unis2})
    if request.method == 'POST':
        if request.POST.get('form_id') == 'form_BuscarUni':
            id_uni = int(request.POST.get('buscarUni_input'))
            temp_uni = Universidad.objects.get(idUniversidad=id_uni)
            form_modificar = UniversidadForm(instance=temp_uni)
            response = HttpResponse()
            response = render(request, 'administracion/CRUD_Universidad/Modificaruni.html', {'unis': unis2, 'form_modificar': form_modificar})
            response.set_cookie('form_activado', 'False')
            return response
        elif request.POST.get('form_id') == 'form_ModUni':
            form_modificar = UniversidadForm(request.POST)
            if form_modificar.is_valid():
                form_modificar.save()
    return response

def administrator_ElUni(request):
    return render(request, 'administracion/CRUD_Universidad/Eliminaruni.html')