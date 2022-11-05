from django import forms

class TipoVehiculoFormulario(forms.Form):

    nombre = forms.CharField(max_length=50)

class VehiculoFormulario(forms.Form):

    marca = forms.CharField(max_length=150)
    modelo=forms.CharField(max_length=150)
    version=forms.CharField(max_length=150)

class SegmentoFormulario(forms.Form):

    nombre = forms.CharField(max_length=50)

