
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("usuarios/", usuarios, name="usuarios"),
    path("temas/", temas, name="temas"),
    path("staff/", staff, name="staff"),
    path("", inicio, name="inicio"),
    path('form_usuarios/', form_usuarios, name='form_usuarios'),
    path('form_staff/', form_staff, name= 'form_staff'),
    path('form_temas/', form_temas, name= 'form_temas'),
    path('busco_usuarios/', busco_usuarios, name= 'busco_usuarios'),
    path('buscando_usuarios/', buscando_usuarios, name ='buscando_usuarios')
]