from django.shortcuts import render
from .models import TipoVehiculo, Vehiculo, Segmento
from django.http import HttpResponseRedirect, HttpResponse
from .forms import TipoVehiculoFormulario, VehiculoFormulario,SegmentoFormulario
def inicio(request):
    
    return render(request, "inicio.html")

def crea_TipoVehiculo(request):

    print('method:', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':

        miFormulario = TipoVehiculoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            tipoVehiculo = TipoVehiculo(name=data['nombre'])
            
            tipoVehiculo.save()

            return HttpResponseRedirect('/app-coder/listaTipoVehiculo/')
    
    else:

        miFormulario = TipoVehiculoFormulario()

        return render(request, "TipoVehiculoCreate.html", {"miFormulario": miFormulario})


def crea_Vehiculo(request):

    print('method:', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':

        miFormulario = VehiculoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            vehiculo = Vehiculo(marca=data['marca'], modelo=data['modelo'], version=data['version'])
            
            vehiculo.save()

            return HttpResponseRedirect('/app-coder/listaVehiculo/')
    
    else:

        miFormulario = VehiculoFormulario()

        return render(request, "VehiculosCreate.html", {"miFormulario": miFormulario})

def crea_Segmento(request):

    print('method:', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':

        miFormulario = SegmentoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            segmento = Segmento(name=data['nombre'])
            
            segmento.save()

            return HttpResponseRedirect('/app-coder/listaSegmento/')
    
    else:

        miFormulario = SegmentoFormulario()

        return render(request, "SegmentosCreate.html", {"miFormulario": miFormulario})


def listaTipoVehiculos(request):

    tipoVehiculos = TipoVehiculo.objects.all()

    return render(request, "ListaTipoVehiculo.html", {"tipoVehiculos": tipoVehiculos})

def listaVehiculos(request):

    vehiculos = Vehiculo.objects.all()

    return render(request, "ListaVehiculo.html", {"vehiculos": vehiculos})

def listaSegmentos(request):

    segmentos = Segmento.objects.all()

    return render(request, "ListaSegmento.html", {"segmentos": segmentos})


def busquedaTipoVehiculo(request):

    return render(request, 'busquedaTipoVehiculo.html')


def resultadoTipoVehiculo(request):
 

    if request.GET["tipoVehiculo"]:

        tipoVehiculo = request.GET["tipoVehiculo"]

        tipoVe = TipoVehiculo.objects.filter(name__icontains=tipoVehiculo)

        return render(request, "resultadobusquedaTipoVehiculo.html", {"tipoVe": tipoVe,"tipoVehiculo": tipoVehiculo})

    else:

        respuesta = "No ingresaste datos"

    return HttpResponse(respuesta)

def busquedaVehiculo(request):

    return render(request, 'busquedaVehiculo.html')


def resultadoVehiculo(request):
 

    if request.GET["marca"]:

        marca = request.GET["marca"]

        vehiculo = Vehiculo.objects.filter(marca__icontains=marca)

        return render(request, "resultadoVehiculo.html", {"vehiculo": vehiculo,"marca": marca})

    else:

        respuesta = "No ingresaste datos"

    return HttpResponse(respuesta)

def busquedaSegmento(request):

    return render(request, 'busquedaSegmento.html')


def resultadoSegmento(request):
 

    if request.GET["segmento"]:

        segmento = request.GET["segmento"]

        segmentoname = Segmento.objects.filter(name__icontains=segmento)

        return render(request, "resultadoSegmento.html", {"segmentoname": segmentoname,"segmento": segmento})

    else:

        respuesta = "No ingresaste datos"

    return HttpResponse(respuesta)