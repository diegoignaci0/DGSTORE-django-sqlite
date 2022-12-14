from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre

class Nike(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre

class Adidas(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre
        
class Puma(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre

opciones_consulta = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre

