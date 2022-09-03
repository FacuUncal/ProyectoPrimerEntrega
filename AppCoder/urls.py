
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("usuarios/", usuarios, name="usuarios"),
    path("temas/", temas, name="temas"),
    path("staff/", staff, name="staff"),
    path("", inicio, name="inicio"),
    
]

#   path("curso/", Curso),
#   path("cursos/", cursos, name="cursos"),