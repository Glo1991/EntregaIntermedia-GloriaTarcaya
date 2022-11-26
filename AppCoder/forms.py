from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.db import models
#from .models import Avatar
from django.shortcuts import render

class TipoVehiculoFormulario(forms.Form):

    nombre = forms.CharField(max_length=50)

class VehiculoFormulario(forms.Form):

    marca = forms.CharField(max_length=150)
    modelo=forms.CharField(max_length=150)
    version=forms.CharField(max_length=150)

class SegmentoFormulario(forms.Form):

    nombre = forms.CharField(max_length=50)

class UserRegisterForm(UserCreationForm):
        first_name=forms.CharField(label="Nombre")
        last_name=forms.CharField(label="Apellido")
        username=forms.CharField(label="Usuario")
        email=forms.EmailField()
        password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
        password2=forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

        class Meta:
            model = User
            fields = ['username', 'last_name', 'first_name', 'email', 'password1', 'password2']
            help_text= {k:"" for k in fields}

class UserViewForm(forms.ModelForm):
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")
    username=forms.CharField(label="Usuario")
    email=forms.EmailField()
    class Meta:

        model = User
        fields = ['username', 'last_name', 'first_name', 'email']
        


class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )
    first_name=forms.CharField(label="Nombre")
    last_name=forms.CharField(label="Apellido")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = [ 'first_name', 'last_name', 'password1', 'password2']


    def clean_password2(self):

        print('self\n',self.cleaned_data)

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden!")
        return password2

class AvatarFormulario(forms.Form):
    imagen=forms.ImageField(label='Imagen:',widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    #imagen = forms.ImageField(widget=forms.CharField(attrs={'class': 'btn-secondary'}))