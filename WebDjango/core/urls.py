from django.urls import path
from .views import index,formsuge,compra,nosotros,venta,creacionuser

urlpatterns = [
    path('',index,name="index"),
    path('index',index,name="index"),
    path('formsuge',formsuge,name="formsuge"),
    path('compra',compra,name="compra"),
    path('nosotros',nosotros,name="nosotros"),
    path('venta',venta,name="venta"),
    path('creacionuser',creacionuser,name="creacionuser"),
]

# path('',,name=""),