from django.db import models

class Domicilio(models.Model):
    direccion = models.CharField(max_length=125, null=False, blank=False)
    ciudad = models.CharField(max_length=100, null=False, blank=False)
    provincia = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "{direccion}, {ciudad}".format(
                direccion=self.direccion,
                ciudad=self.ciudad
            )    

    
class NumeroDeTelefono(models.Model):
    TIPO_DE_LINEA_CHOICES = (
        ('celular', 'Celular'),
        ('fija', 'Fijo')  
    )
    tipo_de_linea = models.CharField(
        max_length=20,
        choices=TIPO_DE_LINEA_CHOICES,
        default=TIPO_DE_LINEA_CHOICES[0][0]
    )        
    numero = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name='Número'
    )

    def __str__(self):
        return self.numero  
    


class Cliente(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    domicilio = models.ForeignKey(
        'Domicilio',
        null=True,
        verbose_name='Domicilio'
    )

    numero_de_telefono = models.ForeignKey(
        'NumeroDeTelefono',
        null=True,
        verbose_name='Número de teléfono'
    )

    def __str__(self):
        return "{} {}".format(self.nombre,self.apellido)


class ClaseEquipo(models.Model):
    '''Representa la clase de dispositivo.
    Ej: teléfono celular, pc, consola'''
    nombre = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        verbose_name = 'Clase de Equipo'

    def __str__(self):
        return self.nombre


class Equipo(models.Model):
    clase = models.ForeignKey('ClaseEquipo', null=False)
    marca = models.CharField(max_length=100, null=True, blank=True)
    modelo = models.CharField(max_length=100, null=True, blank=True)
    codigo_identificador = models.CharField(max_length=100,null=True)
    identificacion_alternativa = models.CharField(
        max_length=200,
        null=True
    )

    def __str__(self):
        return "{marca} {modelo} {cod}".format(
                marca=self.marca,
                modelo=self.modelo,
                cod=self.codigo_identificador
            )

class EstadoTrabajo(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.CharField(max_length=200, null=False, blank=False)

    class Meta:
        verbose_name = 'Estado'

    def __str__(self):
        return self.nombre


class Trabajo(models.Model):
    equipo = models.ForeignKey('Equipo', null=False)
    cliente = models.ForeignKey('Cliente', null=False)
    fecha_de_ingreso = models.DateTimeField(blank=True, null=True)
    fecha_de_salida = models.DateTimeField(blank=True, null=True)
    detalles = models.TextField(max_length=512, null=True, blank=True)
    falla_segun_cliente = models.TextField(max_length=512)
    falla_identificada_por_service = models.TextField(
        max_length=512,
        null=True,
        blank=True
    )
    estado = models.ForeignKey('EstadoTrabajo', null=True)

    def __str__(self):
        return "{equipo} de {cliente} - Falla: {falla}".format(
                equipo=self.equipo,
                cliente=self.cliente,
                falla=self.falla_segun_cliente
            )
