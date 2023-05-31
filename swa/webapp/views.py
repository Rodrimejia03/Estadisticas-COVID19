from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request, 'index.html')

def administrator(request):
    return render(request, 'administracion/base_admin.html')

def administrator_AgEst(request):
    return render(request, 'administracion/Agregarest.html')

def administrator_ModEst(request):
    return render(request, 'administracion/Modificarest.html')

def administrator_ElEst(request):
    return render(request, 'administracion/Eliminarest.html')
