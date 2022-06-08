from django.urls import path
from .views import index,formsuge,compra,nosotros,venta,creacionuser,leer,ventleer,registrarUsuario,modificar
from . import views
urlpatterns = [
    path('',index,name="index"),
    path('index',index,name="index"),
    path('formsuge',formsuge,name="formsuge"),
    path('compra',compra,name="compra"),
    path('nosotros',nosotros,name="nosotros"),
    path('venta',venta,name="venta"),
    path('creacionuser',creacionuser,name="creacionuser"),
    path('leer',leer,name="leer"),
    path('ventleer',ventleer,name="ventleer"),
    path('registrarUsuario/', views.registrarUsuario),
    path('modificar',modificar,name="modificar"),
]

# path('',,name=""),