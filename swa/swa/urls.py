"""swa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from webapp.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name='inicio'),
    #path('2020', year2020, name='2020'),
    path('2021', year2021, name='2021'),
    path('2022', year2022, name='2022'),
    path('login_Admin/', login_Admin, name='login_Admin'),
    path('logout_Admin/', logout_Admin, name='logout_Admin'),
    path('gestionAdmin/', administrator, name='gestionAdmin'),
    path('gestionAdmin/Agregargrf', administrator_AgGrf, name='Agregargrf'),
    path('gestionAdmin/Modificargrf', administrator_ModGrf, name='Modificargrf'),
    path('gestionAdmin/Eliminargrf', administrator_ElGrf, name='Eliminargrf'),
    path('gestionAdmin/Agregaruni', administrator_AgUni, name='Agregaruni'),
    path('gestionAdmin/Modificaruni', administrator_ModUni, name='Modificaruni'),
    path('gestionAdmin/Eliminaruni', administrator_ElUni, name='Eliminaruni'),
]

urlpatterns += staticfiles_urlpatterns()