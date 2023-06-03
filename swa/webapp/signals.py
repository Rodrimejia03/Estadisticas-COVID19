from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Administrador
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