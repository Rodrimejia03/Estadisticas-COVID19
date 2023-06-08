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

def getDatosEstadisticas(anio, cant, tG):
    datos = Estadistica.objects.filter(anio_dato=anio, tipoGrafico=tG)[:cant]
    if datos:
       registros = []
       for dato in datos:
        registro = {
            'anio_dato': dato.anio_dato,
            'tipoGrafico': dato.tipoGrafico,
            'nombreU': dato.idUniversidad.nombreU,
            'numInscritos': dato.idUniversidad.numInscritos,
            'numGraduados': dato.idUniversidad.numGraduados,
            'numDesertados': dato.idUniversidad.numDesertados
        }
        registros.append(registro)
    return registros