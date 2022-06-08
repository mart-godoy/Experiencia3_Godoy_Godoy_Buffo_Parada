from django.shortcuts import render, redirect
from .models import Usuario, Envio

# Create your views here.

def index(request):
    
    return render(request,'core/index.html')

def formsuge(request):
    
    return render(request,'core/formsuge.html')

def compra(request):
    
    return render(request,'core/compra.html')


def nosotros(request):
    
    return render(request,'core/nosotros.html')


def venta(request):
    data= {
        'venta': Formvent()
    }

    if request.method== 'POST':
        ventaformulario = Formvent(request.POST)
        if ventaformulario.is_valid:
            Formvent.save()

    return render(request,'core/venta.html',data)

def creacionuser(request):



    return render(request,'core/creacionuser.html')

def leer(request):
    
    usuariosLista = Usuario.objects.all()
    return render(request,"core/leer.html",{"usuarios": usuariosLista})

def ventleer(request):

    envios = Envio.objects.all()

    datos= {
        'envios': envios
    }
    return render(request, 'core/ventleer.html',datos)

def registrarUsuario(request):
    usuario = request.POST['usuario']
    nombre = request.POST['nombre']
    password = request.POST['password']
    correo = request.POST['correo']
    telefono = request.POST['telefono']

    usuario = Usuario.objects.create(usuario=usuario,nombre=nombre,password=password,correo=correo,telefono=telefono)

    return redirect('/')