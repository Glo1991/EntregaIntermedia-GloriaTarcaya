from django.shortcuts import render
from .models import TipoVehiculo, Vehiculo, Segmento, Avatar
from django.http import HttpResponseRedirect, HttpResponse
from .forms import TipoVehiculoFormulario, VehiculoFormulario,SegmentoFormulario, UserRegisterForm, UserEditForm, UserViewForm, AvatarFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import  get_object_or_404

def inicio(request):
    #print(Avatar.objects.filter(user=request.user.id)[0].imagen.url)
    #avatares=Avatar.objects.filter(user=request.user.id)
    #return render(request, "inicio.html", {"url": avatares[0].imagen.url})
    return render(request, "inicio.html")

#@staff_member_required(login_url="/app-coder/login")
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

@staff_member_required(login_url="/app-coder/listaVehiculo")
def crea_Vehiculo(request):

    print('method:', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':

        miFormulario = VehiculoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            vehiculo = Vehiculo(idSegmento=data['idSegmento'], idTipoVehiculo=data['idTipoVehiculo'], marca=data['marca'], modelo=data['modelo'], version=data['version'])
            print (f'esto manda {Vehiculo}')
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

def login_request (request):
    print('method:', request.method)
    print('post: ', request.POST)
    if request.method=="POST":
        miFormulario=AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)
            if user:

                login(request, user)

                return render(request, "inicio.html", {"mensaje": f'Bienvenido {usuario}'})
            
            else:

                return render(request, "inicio.html", {"mensaje": f'Error, datos incorrectos'})

        return render(request, "inicio.html", {"mensaje": f'Error, formulario invalido'})

    else:

        miFormulario = AuthenticationForm()

        return render(request, "login.html", {"miFormulario": miFormulario})

def register(request):

    print('method:', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':

        miFormulario = UserRegisterForm(request.POST)
        
        if miFormulario.is_valid():

            username = miFormulario.cleaned_data["username"]

            miFormulario.save()
            
            miFormulariologin=AuthenticationForm(request, data=request.POST)
            return render(request, "login.html", {"miFormulario": miFormulariologin})

        else:
           
            return render(request, "inicio.html", {"mensaje": f'Error al crear el usuario'})

    else:

        miFormulario = UserRegisterForm()

        return render(request, "registro.html", {"miFormulario": miFormulario})

def about(request):

    return render(request, "about.html")



def editar_perfil(request):
    
    print('method:', request.method)
    print('post: ', request.POST)

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.set_password(data["password1"])

            usuario.save()
            update_session_auth_hash(request, usuario)
            miFormularioVerPErfil = UserViewForm(instance=request.user)
            return render(request, "perfil.html", {"miFormulario": miFormularioVerPErfil})
        
        return render(request, "perfil.html", {"mensaje": 'Contraseñas no coinciden'} )
    
    else:

        miFormulario = UserEditForm(instance=request.user)

        return render(request, "editarPerfil.html", {"miFormulario": miFormulario})

def ver_perfil(request):

        miFormulario = UserViewForm(instance=request.user)

        return render(request, "perfil.html", {"miFormulario": miFormulario})


def agregar_avatar(request):

    if request.method == 'POST':
        try: 
            avatar_inicial= Avatar.objects.get(user=request.user)
        #avatar_inicial=get_object_or_404(Avatar, user=request.user)
            print(avatar_inicial)    
        except:    
            avatar_inicial=None
        
        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            if avatar_inicial==None:
               
                u = User.objects.get(username=request.user)
                avatar = Avatar( user=u, imagen= miFormulario.cleaned_data['imagen'])
                print(u, avatar)
                avatar.save()
            else:
                avatar_inicial.imagen= miFormulario.cleaned_data['imagen']
                avatar_inicial.save()

            miFormularioVerPErfil = UserViewForm(instance=request.user)
            return render(request, "perfil.html", {"miFormulario": miFormularioVerPErfil})
        
        return render(request, "perfil.html", {"mensaje": 'Contraseñas no coinciden'} )
    
    else:

        miFormulario = AvatarFormulario()

        return render(request, "agregarAvatar.html", {"miFormulario": miFormulario})

def eliminar_avatar(request):
    avatar = Avatar.objects.get(user=request.user)
    print(request.method)
    if request.method == 'POST':

        print (avatar)
        avatar.delete()

        miFormularioVerPErfil = UserViewForm(instance=request.user)
        print('paso por aqui')
        return render(request, "perfil.html", {"miFormulario": miFormularioVerPErfil})  
    
    else:
        
        return render(request, "eliminarAvatar.html",{"avatar": avatar})
    
def tipsVehiculos(request):

    return render(request, 'TipsVehiculos.html')

def novedadesVehiculos(request):

    return render(request, 'novedadesVehiculos.html')
