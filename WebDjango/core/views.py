from django.shortcuts import render

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
