from django.urls import path
from .views import index,formsuge,compra,nosotros,venta,creacionuser,leer,ventleer,registrarUsuario,modUsuario,modifUsuario,registrarEnvio,modifEnvioo,modEnvioo
from . import views
urlpatterns = [
    path('',index,name="index"),
    path('index',index,name="index"),
    path('formsuge',formsuge,name="formsuge"),
    path('nosotros',nosotros,name="nosotros"),
    path('compra',compra,name="compra"),
    path('venta',venta,name="venta"),
    path('registrarEnvio/', registrarEnvio,name="registrarEnvio"),
    path('modEnvioo/', views.modEnvioo, name="modEnvioo"),
    path('modifEnvioo/', views.modifEnvioo, name="modifEnvioo"),
    path('ventleer',ventleer,name="ventleer"),
    path('creacionuser',creacionuser,name="creacionuser"),
    path('leer',leer,name="leer"),
    path('registrarUsuario/', views.registrarUsuario),
    path('modUsuario/', modUsuario, name="modUsuario"),
    path('modifUsuario/', modifUsuario, name="modifUsuario"),
]

# path('',,name=""),