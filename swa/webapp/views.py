from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import  login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from webapp.authentication.auth_backend import AdministradorAuthBackend
from .utils import *
from .models import *

Admin = Administrador()

# Create your views here.
def welcome(request):
    temp_anio = 2020
    unis = Universidad.objects.get(idUniversidad=1)
    return render(request, 'index.html', {'unis': unis})

def login_Admin(request):
    if request.method == 'POST' and request.POST.get('login_ad') == 'login_1':
        email1 = request.POST.get('email_admin')
        password = request.POST.get('password_admin')
        next_url = request.POST.get('next') 
    
        user = AdministradorAuthBackend().authenticate(request, email=email1, password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            Admin = Administrador.objects.get(email=email1)
            return redirect('gestionAdmin')
        else:
             return render(request, 'login.html', {'error': 'Datos invalidos'})
    return render(request, 'login.html')

def logout_Admin(request):
    logout(request)
    return redirect('inicio')

@login_required
def administrator(request):
     
     return render(request, 'administracion/admin_general.html', {'datos_generales': getCountDatos() , 'id_Admin': Admin})

@login_required
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

@login_required
def administrator_ModGrf(request):
    grafis = Estadistica.objects.all()
    unis = Universidad.objects.all()
    form_deshabilitado = 1
    form_modificar = GraficoForm(initial={})
    response =  render(request, 'administracion/CRUD_Grafico/Modificargrf.html', {'grafis': grafis, 'unis': unis, 'form_deshabilitado': form_deshabilitado})
    if request.method == 'POST':
        if request.POST.get('form_id') == 'form_BuscarGrf':
            id_Grf = request.POST.get('buscarGrf_input')
            temp_grf = Estadistica.objects.get(idEstadistica=id_Grf)
            form_modificar = GraficoForm(instance=temp_grf)
            form_deshabilitado = 0
            response = render(request, 'administracion/CRUD_Grafico/Modificargrf.html', {'grafis': grafis, 'unis': unis, 'form_modificar': form_modificar ,'form_deshabilitado': form_deshabilitado, 'id_Grf_l': id_Grf})
        elif request.POST.get('form_id') == "form_ModGrf":
            id_Grf2 = request.POST.get('id-Estadistica')
            temp_anio  = request.POST.get('anio_input')
            temp_tipoG = request.POST.get('tipoGrafico_input')
            temp_idUniversidad = request.POST.get('universidad_input')
            form_modificar2 = Estadistica.objects.get(idEstadistica=id_Grf2)
            if not Estadistica.objects.filter(anio_dato=temp_anio, tipoGrafico=temp_tipoG, idUniversidad=temp_idUniversidad).exclude(idEstadistica=id_Grf2):
                form_modificar2.anio_dato = temp_anio
                form_modificar2.tipoGrafico = temp_tipoG
                form_modificar2.idUniversidad_id = temp_idUniversidad
                form_modificar2.save()
                messages.success(request, 'Grafico modificado correctamente.')
            else:
                messages.error(request, 'Error al modificar el grafico,  Asegurate que no estas digitando los mismos valores')
            response = render(request, 'administracion/CRUD_Grafico/Modificargrf.html', {'grafis': grafis, 'unis': unis,'form_deshabilitado': form_deshabilitado})
    return response

@login_required
def administrator_ElGrf(request):
    grafis = Estadistica.objects.all()
    return render(request, 'administracion/CRUD_Grafico/Eliminargrf.html', {'grafis': grafis})

@login_required
def administrator_AgUni(request):
    if request.method == 'POST' and request.POST.get('form_id') == 'form_AgregarUni':
        temp_uni = Universidad()
        temp_uni.nombreU = request.POST.get('nombreU_input')
        temp_uni.anio_periodo = request.POST.get('anio_periodo_input')
        if not Universidad.objects.filter(nombreU=temp_uni.nombreU, anio_periodo=temp_uni.anio_periodo):
            temp_uni.numInscritos = request.POST.get('inscritos_input')
            temp_uni.numGraduados = request.POST.get('graduados_input')
            temp_uni.numDesertados = request.POST.get('desertados_input')
            temp_uni.save()
            messages.success(request, 'Datos guardados correctamente.')
        else:
            messages.error(request, 'Error al guardar los datos, Ya hay datos existentes')
    return render(request, 'administracion/CRUD_Universidad/Agregaruni.html')

@login_required
def administrator_ModUni(request):
    unis = Universidad.objects.all()
    form_deshabilitado = 1
    form_modificar = UniversidadForm(initial={})
    response =  render(request, 'administracion/CRUD_Universidad/Modificaruni.html', {'unis': unis, 'form_deshabilitado': form_deshabilitado})
    if request.method == 'POST':
        if request.POST.get('form_id') == 'form_BuscarUni':
            id_uni = int(request.POST.get('buscarUni_input'))
            temp_uni = Universidad.objects.get(idUniversidad=id_uni)
            form_modificar = UniversidadForm(instance=temp_uni)
            form_deshabilitado = 0
            response = render(request, 'administracion/CRUD_Universidad/Modificaruni.html', {'unis': unis, 'form_modificar': form_modificar, 'form_deshabilitado': form_deshabilitado, 'id_uni_l': id_uni})
        elif request.POST.get('form_id') == 'form_ModUni':
            id_uni = request.POST.get('id-Universidad')
            temp_nombreU = request.POST.get('nombreU_input')
            temp_anio = request.POST.get('anio_periodo_input')
            form_modificar2 = Universidad.objects.get(idUniversidad=id_uni)
            if not Universidad.objects.filter(nombreU=temp_nombreU, anio_periodo=temp_anio).exclude(idUniversidad=id_uni):
                temp_numD = request.POST.get('desertados_input')
                temp_numI = request.POST.get('inscritos_input')
                temp_numG = request.POST.get('graduados_input')
                form_modificar2.nombreU = temp_nombreU
                form_modificar2.anio_periodo = temp_anio
                form_modificar2.numDesertados = temp_numD
                form_modificar2.numInscritos = temp_numI
                form_modificar2.numGraduados = temp_numG
                form_modificar2.save()
                messages.success(request, 'Universidad Modificada correctamente.')
            else:
                messages.error(request, 'Error al modificar la universidad seleccionada, Asegurate que no estas digitando los mismos valores')
            response = render(request, 'administracion/CRUD_Universidad/Modificaruni.html', {'unis': unis, 'form_deshabilitado': form_deshabilitado})
    return response

@login_required
def administrator_ElUni(request):
    return render(request, 'administracion/CRUD_Universidad/Eliminaruni.html')