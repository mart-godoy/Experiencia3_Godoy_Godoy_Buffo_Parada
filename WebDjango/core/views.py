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


    return render(request,'core/venta.html')

def creacionuser(request):
    
    return render(request,'core/creacionuser.html')

def leer(request):

    usuariosLista = Usuario.objects.all()
    return render(request,"core/leer.html",{"usuarios": usuariosLista})
    
def modUsuario(request):

    usuarioMod = Usuario.objects.all()
    return render(request,"core/modUsuario.html",{"modificara":usuarioMod})

def modifUsuario(request):
    usuario = request.POST['usuario']
    nombre = request.POST['nombre']
    password = request.POST['password']
    correo = request.POST['correo']
    telefono = request.POST['telefono']

    usuarioMod = Usuario.objects.all()
    usuarioMod.usuario = usuario
    usuarioMod.nombre = nombre
    usuarioMod.password = password
    usuarioMod.correo = correo
    usuarioMod.telefono = telefono
    usuarioMod.save()

    return redirect('/')

def ventleer(request):

    enviosLista = Envio.objects.all()
    return render(request,"core/ventleer.html",{"envios": enviosLista})


def registrarUsuario(request):
    usuario = request.POST['usuario']
    nombre = request.POST['nombre']
    password = request.POST['password']
    correo = request.POST['correo']
    telefono = request.POST['telefono']

    usuario = Usuario.objects.create(usuario=usuario,nombre=nombre,password=password,correo=correo,telefono=telefono)

    return redirect('/')


def registrarEnvio(request):
    rut = request.POST['rut']
    nombre = request.POST['nombre']
    email = request.POST['email']
    phone = request.POST['phone']
    ciudad = request.POST['ciudad']
    comuna = request.POST['comuna']
    calle = request.POST['calle']
    casa = request.POST['casa']

    envios = Envio.objects.create(
        rut=rut, nombre=nombre, email=email, phone=phone, ciudad=ciudad,
        comuna=comuna,calle=calle,casa=casa
    )

    return redirect('/')

def modEnvioo(request):

    envioMod = Usuario.objects.all()
    return render(request,"core/modEnvio.html",{"modificar":envioMod})

def modifEnvioo(request):
    rut = request.POST['rut']
    nombre = request.POST['nombre']
    email = request.POST['email']
    phone = request.POST['phone']
    ciudad = request.POST['ciudad']
    comuna = request.POST['comuna']
    calle = request.POST['calle']
    casa = request.POST['casa']

    envioMod = Envio.objects.all()
    envioMod.rut = rut
    envioMod.nombre = nombre
    envioMod.email = email
    envioMod.phone = phone
    envioMod.ciudad = ciudad
    envioMod.comuna = comuna
    envioMod.calle = calle
    envioMod.casa = casa
    envioMod.save()

    return redirect('/')