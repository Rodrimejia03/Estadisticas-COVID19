from django import forms
from .models import *

class UniversidadForm(forms.ModelForm):
    class Meta:
        model = Universidad
        fields = fields = ("anio_periodo", "nombreU", "numDesertados", "numGraduados", "numInscritos")
        # Aquí se especifican los campos que se mostrarán en el formulario

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