from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

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
