from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    cedula = models.CharField(max_length=10, unique=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    correo = models.EmailField(unique=True, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    
    def get_full_name(self):
        return f'{self.nombre} {self.apellido}'

    def __str__(self):
        return self.get_full_name()

class Vehiculo(models.Model):
    marca = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    anio = models.PositiveIntegerField(verbose_name='año')  
    color = models.CharField(max_length=50, blank=True, null=True)
    placa = models.CharField(max_length=10, unique=True, null=True)
    propietario = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='vehiculos')
    
    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.anio})'

class Alquiler(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('En curso', 'En curso'), ('Finalizado', 'Finalizado')])

    def __str__(self):
        return f"Alquiler de {self.vehiculo} por {self.cliente}"

class Reparacion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField(blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('Pendiente', 'Pendiente'), ('En progreso', 'En progreso'), ('Completado', 'Completado')])

    def __str__(self):
        return f"Reparación de {self.vehiculo} - {self.estado}"

class Mantenimiento(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Mantenimiento de {self.vehiculo} - {self.fecha}"
