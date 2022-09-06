from django import forms

class UsuariosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    nickname = forms.CharField(max_length=50)
    email = forms.EmailField()

class TemasForm(forms.Form):
    tema_1 = forms.CharField(max_length=50)
    tema_2 = forms.CharField(max_length=50)
    tema_3 = forms.CharField(max_length=50)
    tema_4 = forms.CharField(max_length=50)

class StaffForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    nickname = forms.CharField(max_length=50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)
    area_control = forms.CharField(max_length=50)
