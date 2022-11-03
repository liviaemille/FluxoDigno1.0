from django.contrib import admin
from .models import usuarioDoador, pontosColeta, Doacoes

# Register your models here.
admin.site.register(usuarioDoador)
admin.site.register(pontosColeta)
admin.site.register(Doacoes)
