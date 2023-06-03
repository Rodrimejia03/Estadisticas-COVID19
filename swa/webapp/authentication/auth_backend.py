from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from ..models import Administrador

class AdministradorAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            administrador = Administrador.objects.get(email=email)
            
            if check_password(password, administrador.contrasenia):
                return administrador
            else:
                return None
                
        except Administrador.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Administrador.objects.get(idAdmin=user_id)
        except Administrador.DoesNotExist:
            return None
    def get_by_natural_key(self, email):
        return self.get(email=email)