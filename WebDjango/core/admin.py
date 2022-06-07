from django.contrib import admin
from .models import Envio, Usuario
# Register your models here.

#Administrar el modelo completo

admin.site.register(Usuario)
admin.site.register(Envio)