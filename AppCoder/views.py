import http
from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpRequest
# Create your views here.



def inicio(request):
    return render (request, "AppCoder/inicio.html")

#def cursos(request):
 #   return render (request, "AppCoder/cursos.html")

#def usuarios(request):
    #clas1 = clase1(var1="prueba1")
    #clas1.save()
    #txt= f"se logro guardar"
    #return HttpResponse (txt)

#def temas (request):
    #clas2 = clase2(var2=999)
    #clas2.save()
    #txt= f"se logro guardar clase 2"
    #return HttpResponse (txt)

#def staff (request):
    #clas3 = clase3(var3="1800-01-01")
    #clas3.save()
    #txt= f"se logro guardar clase 3"
    #return HttpResponse (txt)

def usuarios(request):
    return render(request, "AppCoder/usuarios.html")

def temas(request):
    return render(request, "AppCoder/temas.html")

def staff(request):
    return render(request, "AppCoder/staff.html")
