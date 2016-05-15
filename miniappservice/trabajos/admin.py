from django.contrib import admin

from .models import ClaseEquipo, Cliente, NumeroDeTelefono, Domicilio,\
                    Equipo, Trabajo, EstadoTrabajo


@admin.register(ClaseEquipo)
class ClaseEquipoAdmin(admin.ModelAdmin):
    pass


# Habilitados temporariamente

@admin.register(Domicilio)
class DomicilioAdmin(admin.ModelAdmin):
    pass
    
   
@admin.register(NumeroDeTelefono)
class NumeroDeTelefonoAdmin(admin.ModelAdmin):
    pass


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    pass


@admin.register(Trabajo)
class TrabajoAdmin(admin.ModelAdmin):
    pass


@admin.register(EstadoTrabajo)
class EstadoTrabajoAdmin(admin.ModelAdmin):
    pass
