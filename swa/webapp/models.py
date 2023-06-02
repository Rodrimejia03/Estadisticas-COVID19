from django.db import models

class Universidad(models.Model):
    idUniversidad = models.AutoField(primary_key=True)
    anio_periodo = models.IntegerField()
    nombreU = models.CharField(max_length=50)
    numDesertados = models.IntegerField()
    numGraduados = models.IntegerField()
    numInscritos = models.IntegerField()

class Administrador(models.Model):
    idAdmin = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    contrasenia = models.CharField(max_length=120)

class Estadistica(models.Model):
    idEstadistica = models.AutoField(primary_key=True)
    anio_dato = models.IntegerField()
    tipoGrafico = models.CharField(max_length=25)
    idAdmin = models.ForeignKey(Administrador, on_delete=models.CASCADE)
    idUniversidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)