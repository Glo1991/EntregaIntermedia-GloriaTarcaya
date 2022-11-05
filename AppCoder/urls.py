from django.contrib import admin
from django.urls import path, include
from .views import inicio, crea_TipoVehiculo, crea_Segmento, crea_Vehiculo, listaTipoVehiculos, listaSegmentos,listaVehiculos, resultadoTipoVehiculo, busquedaTipoVehiculo, busquedaVehiculo, busquedaSegmento,resultadoSegmento, resultadoVehiculo

urlpatterns = [
    path('', inicio, name='Inicio'),
    path('crea-tipoVehiculo/', crea_TipoVehiculo, name="TipoVehiculoCrear"),
    path('crea-Vehiculo/', crea_Vehiculo , name="VehiculoCrear"),
    path('crea-segmento/',crea_Segmento , name="SegmentoCrear"),
    path('listaTipoVehiculo/',listaTipoVehiculos , name="ListaTipoVehiculo"),
    path('listaVehiculo/',listaVehiculos , name="ListaVehiculo"),
    path('listaSegmento/',listaSegmentos , name="ListaSegmento"),
    path('buscarTipoVehiculo/', busquedaTipoVehiculo, name="BuscarTipoVehiculo"),
    path('buscarVehiculo/', busquedaVehiculo, name="BuscarVehiculo"),
    path('buscarSegmento/',busquedaSegmento , name="BuscarSegmento"),
    path('resultadoTipoVehiculo/', resultadoTipoVehiculo, name="resultadoTipoVehiculo"),
    path('resultadoVehiculo/', resultadoVehiculo, name="resultadoVehiculo"),
    path('resultadoSegmento/', resultadoSegmento, name="resultadoSegmento"),
]
