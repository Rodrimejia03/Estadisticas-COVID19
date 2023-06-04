from django import forms
from .models import *

class UniversidadForm(forms.ModelForm):
    class Meta:
        model = Universidad
        fields = ("anio_periodo", "nombreU", "numDesertados", "numGraduados", "numInscritos")

class GraficoForm(forms.ModelForm):
    class  Meta:
        model = Estadistica
        fields = ("anio_dato", "tipoGrafico", "idUniversidad")

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