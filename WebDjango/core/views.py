from django.shortcuts import render
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
    
    if request.method== 'POST':
        ventaformulario = Formvent(request.POST)
        if ventaformulario.is_valid:
            Formvent.save()

    return render(request,'core/venta.html',datos)

def creacionuser(request):

    if request.method== 'POST':
        
        formularios = Formulario(request.POST)
        if formularios.is_valid:
            formulario.save()
    return render(request,'core/creacionuser.html',datos)

def leer(request):
    
    usuarios= Usuario.objects.all()

    datos = {
        'usuarios': usuarios
    }

    return render(request, 'core/leer.html',datos)

def ventleer(request):

    envios = Envio.objects.all()

    datos= {
        'envios': envios
    }
    return render(request, 'core/ventleer.html',datos)