from django.forms import ModelForm, NumberInput
from .models import *

def getCountDatos():
    countUni = Universidad.objects.count()
    countAdmin = Administrador.objects.count()
    countGrafico = Estadistica.objects.count()

    dic_datos = {
        "Universidad": countUni,
        "Administrador": countAdmin,
        "Grafico": countGrafico
    }

    return dic_datos