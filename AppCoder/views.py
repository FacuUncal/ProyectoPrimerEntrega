from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpRequest
from AppCoder.forms import *
# Create your views here.


def inicio(request):
    return render (request, "AppCoder/inicio.html")

def usuarios(request):
    return render(request, "AppCoder/usuarios.html")

def temas(request):
    return render(request, "AppCoder/temas.html")

def staff(request):
    return render(request, "AppCoder/staff.html")

def form_usuarios(request):
    if request.method=="POST":
        form=UsuariosForm(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            nickname=informacion["nickname"]
            email=informacion["email"]
            usuario = Usuarios(nombre=nombre, apellido=apellido,nickname=nickname, email=email)
            usuario.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        formulario=UsuariosForm()
        return render (request, "AppCoder/form_usuarios.html", {"formulario":formulario})

def form_staff(request):
    if request.method=="POST":
        form=StaffForm(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre"]
            apellido=informacion["apellido"]
            nickname=informacion["nickname"]
            email=informacion["email"]
            area_control = informacion ['area_control']
            profesion = informacion ['profesion']
            staff = Staff(nombre=nombre, apellido=apellido,nickname=nickname, email=email, area_control=area_control, profesion=profesion)
            staff.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        formulario=StaffForm()
        return render (request, "AppCoder/form_staff.html", {"formulario":formulario})

def form_temas(request):
    if request.method=="POST":
        form=TemasForm(request.POST)

        if form.is_valid():
            informacion=form.cleaned_data
            tema_1=informacion["tema_1"]
            tema_2=informacion["tema_2"]
            tema_3=informacion["tema_3"]
            tema_4=informacion["tema_4"]
            temas = Temas(tema_1=tema_1, tema_2=tema_2, tema_3=tema_3, tema_4=tema_4)
            temas.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        formulario=TemasForm()
        return render (request, "AppCoder/form_temas.html", {"formulario":formulario})

def busco_usuarios(request):
    return render(request, 'AppCoder/busco_usuarios.html')

def buscando_usuarios(request):
    if request.GET['nickname']:
        nickname = request.GET['nickname']
        usuarios=Usuarios.objects.filter(nickname=nickname)
        return render(request, 'AppCoder/res_b_usuarios.html', {'Usuarios': usuarios})
    else:
        return render(request, 'AppCoder/busco_usuarios.html', {'mensaje': 'Ingrese un usuario'})