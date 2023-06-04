from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import *
from django.contrib.auth.hashers import make_password


@receiver(post_migrate)
def crear_instancias_administrador(sender, **kwargs):
    if sender.name == 'webapp': 
        if not Administrador.objects.exists():
            instancias = [
                {'email': 'mm20191@ues.edu.sv', 'contrasenia': 'rodri1234'},
                {'email': 'rg18081@ues.edu.sv', 'contrasenia': 'marvin1234'},
                {'email': 'hm19066@ues.edu.sv', 'contrasenia': 'kathe1234'},
            ]
            for instancia in instancias:
                instancia['contrasenia'] = make_password(instancia['contrasenia'])
                Administrador.objects.create(email=instancia['email'], contrasenia=instancia['contrasenia'])

@receiver(post_migrate)
def crear_instancias_universidad(sender, **kwargs):
    if sender.name == 'webapp': 
        if not Universidad.objects.exists():
            instancias = [
                {'anio_periodo': '2020',
                'nombreU': 'Universidad de El Salvador',
                'numDesertados': 740,
                'numGraduados': 1230,
                'numInscritos': 54531
                },
                {'anio_periodo': '2020',
                'nombreU': 'Universidad Tecnologica de El Salvador',
                'numDesertados': 550,
                'numGraduados': 1339,
                'numInscritos': 11530
                },
                {'anio_periodo': '2020',
                'nombreU': 'Univesidad Don Bosco',
                'numDesertados': 468,
                'numGraduados': 1203,
                'numInscritos': 15600
                },
                {'anio_periodo': '2020',
                'nombreU': 'Universidad Alberto Masferrer',
                'numDesertados': 500,
                'numGraduados': 413,
                'numInscritos': 12300
                },
                {'anio_periodo': '2020',
                'nombreU': 'Universidad Fransico Gavidia',
                'numDesertados': 286,
                'numGraduados': 1209,
                'numInscritos': 12960
                },
                {'anio_periodo': '2020',
                'nombreU': 'Universidad Pedagogica de El Salvador',
                'numDesertados': 405,
                'numGraduados': 402,
                'numInscritos': 9780
                },
                {'anio_periodo': '2020',
                'nombreU': 'Universidad Dr. Jose Matias Delgado',
                'numDesertados': 255,
                'numGraduados': 595,
                'numInscritos': 11020
                },
                {'anio_periodo': '2020',
                'nombreU': 'Universidad Andres Bello',
                'numDesertados': 473,
                'numGraduados': 1895,
                'numInscritos': 13400
                },
                {'anio_periodo': '2020',
                'nombreU': 'Universidad Gerardo Barrios',
                'numDesertados': 503,
                'numGraduados': 1319,
                'numInscritos': 10203
                },
                {'anio_periodo': '2021',
                'nombreU': 'Universidad de El Salvador',
                'numDesertados': 2100,
                'numGraduados': 724,
                'numInscritos': 55407
                },
                {'anio_periodo': '2021',
                'nombreU': 'Universidad Tecnologica de El Salvador',
                'numDesertados': 734,
                'numGraduados': 594,
                'numInscritos': 6571
                },
                {'anio_periodo': '2021',
                'nombreU': 'Univesidad Don Bosco',
                'numDesertados': 705,
                'numGraduados': 472,
                'numInscritos': 10747
                },
                {'anio_periodo': '2021',
                'nombreU': 'Universidad Alberto Masferrer',
                'numDesertados': 861,
                'numGraduados': 666,
                'numInscritos': 13633
                },
                {'anio_periodo': '2021',
                'nombreU': 'Universidad Fransico Gavidia',
                'numDesertados': 1162,
                'numGraduados': 1355,
                'numInscritos': 11945
                },
                {'anio_periodo': '2021',
                'nombreU': 'Universidad Pedagogica de El Salvador',
                'numDesertados': 744,
                'numGraduados': 250,
                'numInscritos': 17360
                },
                {'anio_periodo': '2021',
                'nombreU': 'Universidad Dr. Jose Matias Delgado',
                'numDesertados': 962,
                'numGraduados': 711,
                'numInscritos': 12870
                },
                {'anio_periodo': '2021',
                'nombreU': 'Universidad Andres Bello',
                'numDesertados': 519,
                'numGraduados': 668,
                'numInscritos': 15653
                },
                {'anio_periodo': '2021',
                'nombreU': 'Universidad Gerardo Barrios',
                'numDesertados': 578,
                'numGraduados': 788,
                'numInscritos': 16407
                },
                {'anio_periodo': '2022',
                'nombreU': 'Universidad de El Salvador',
                'numDesertados': 619,
                'numGraduados': 792,
                'numInscritos': 51880
                },
                {'anio_periodo': '2022',
                'nombreU': 'Universidad Tecnologica de El Salvador',
                'numDesertados': 614,
                'numGraduados': 1045,
                'numInscritos': 9800
                },
                {'anio_periodo': '2022',
                'nombreU': 'Univesidad Don Bosco',
                'numDesertados': 631,
                'numGraduados': 760,
                'numInscritos': 23400
                },
                {'anio_periodo': '2022',
                'nombreU': 'Universidad Alberto Masferrer',
                'numDesertados': 879,
                'numGraduados': 791,
                'numInscritos': 15300
                },
                {'anio_periodo': '2022',
                'nombreU': 'Universidad Fransico Gavidia',
                'numDesertados': 877,
                'numGraduados': 959,
                'numInscritos': 11178
                },
                {'anio_periodo': '2022',
                'nombreU': 'Universidad Pedagogica de El Salvador',
                'numDesertados': 730,
                'numGraduados': 712,
                'numInscritos': 13020
                },
                {'anio_periodo': '2022',
                'nombreU': 'Universidad Dr. Jose Matias Delgado',
                'numDesertados': 728,
                'numGraduados': 971,
                'numInscritos': 13205
                },
                {'anio_periodo': '2022',
                'nombreU': 'Universidad Andres Bello',
                'numDesertados': 618,
                'numGraduados': 905,
                'numInscritos': 11300
                },
                {'anio_periodo': '2022',
                'nombreU': 'Universidad Gerardo Barrios',
                'numDesertados': 884,
                'numGraduados': 1094,
                'numInscritos': 10023
                }
            ]
            for instancia in instancias:
                Universidad.objects.create(anio_periodo=instancia['anio_periodo'], 
                                           nombreU=instancia['nombreU'],
                                           numDesertados=instancia['numDesertados'],
                                           numGraduados=instancia['numGraduados'],
                                           numInscritos=instancia['numInscritos'],)
@receiver(post_migrate)
def crear_instancias_Estadistica(sender, **kwargs):
    if sender.name == 'webapp': 
        if not Estadistica.objects.exists():
            instancias = [
                {'anio_dato': 2020, 'tipoGrafico': 'Barras', 'idUniversidad_id': 1, 'idAdmin_id': 1},
                {'anio_dato': 2020, 'tipoGrafico': 'Barras', 'idUniversidad_id': 2, 'idAdmin_id': 1},
                {'anio_dato': 2020, 'tipoGrafico': 'Barras', 'idUniversidad_id': 3, 'idAdmin_id': 1},
                {'anio_dato': 2021, 'tipoGrafico': 'Barras', 'idUniversidad_id': 10, 'idAdmin_id': 1},
                {'anio_dato': 2021, 'tipoGrafico': 'Barras', 'idUniversidad_id': 11, 'idAdmin_id': 1},
                {'anio_dato': 2021, 'tipoGrafico': 'Barras', 'idUniversidad_id': 12, 'idAdmin_id': 1},
                {'anio_dato': 2022, 'tipoGrafico': 'Barras', 'idUniversidad_id': 19, 'idAdmin_id': 1},
                {'anio_dato': 2022, 'tipoGrafico': 'Barras', 'idUniversidad_id': 20, 'idAdmin_id': 1},
                {'anio_dato': 2022, 'tipoGrafico': 'Barras', 'idUniversidad_id': 21, 'idAdmin_id': 1},
                
                {'anio_dato': 2020, 'tipoGrafico': 'Pastel', 'idUniversidad_id': 1, 'idAdmin_id': 1},
                {'anio_dato': 2020, 'tipoGrafico': 'Pastel', 'idUniversidad_id': 2, 'idAdmin_id': 1},
                {'anio_dato': 2020, 'tipoGrafico': 'Pastel', 'idUniversidad_id': 3, 'idAdmin_id': 1},
                {'anio_dato': 2021, 'tipoGrafico': 'Pastel', 'idUniversidad_id': 10, 'idAdmin_id': 1},
                {'anio_dato': 2021, 'tipoGrafico': 'Pastel', 'idUniversidad_id': 11, 'idAdmin_id': 1},
                {'anio_dato': 2021, 'tipoGrafico': 'Pastel', 'idUniversidad_id': 12, 'idAdmin_id': 1},
                {'anio_dato': 2022, 'tipoGrafico': 'Pastel', 'idUniversidad_id': 19, 'idAdmin_id': 1},
                {'anio_dato': 2022, 'tipoGrafico': 'Pastel', 'idUniversidad_id': 20, 'idAdmin_id': 1},
                {'anio_dato': 2022, 'tipoGrafico': 'Pastel', 'idUniversidad_id': 21, 'idAdmin_id': 1},

            ]
            for instancia in instancias:
                Estadistica.objects.create(anio_dato=instancia['anio_dato'],
                                           tipoGrafico=instancia['tipoGrafico'], 
                                           idUniversidad_id=instancia['idUniversidad_id'],
                                           idAdmin_id=instancia['idAdmin_id'])
