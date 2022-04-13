from django.db import models
from datetime import datetime

from django.forms import model_to_dict
from App.erp.choices import gender_choices


# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc=models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripción')

    def __str__(self):
        return self.name

    def toJSON(self):
        # item = {'id':self.id, 'name':self.name, 'descripcion':self.desc} es una forma, la segunda es usar el método model_to_dict
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categoria'
        #db_table='empleado'
        ordering=['id']

class Product(models.Model):
    name=models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate=models.ForeignKey(Category, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp=models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        ordering=['id']


class Client(models.Model):
    names=models.CharField(max_length=150, verbose_name='Nombres')
    surnames=models.CharField(max_length=150, verbose_name='Apellidos')
    dni=models.CharField(max_length=150, verbose_name='Dni')
    birthday=models.DateField(default=datetime.now, verbose_name='Fecha Nacimiento')
    address=models.CharField(max_length=150, verbose_name='Direccion', null=True, blank=True)
    sexo=models.CharField(max_length=10, verbose_name='Sexo', default='male', choices=gender_choices)

    def __str__(self):
        return self.names
    
    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'
        ordering=['id']

class Sale(models.Model):
    cli=models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined=models.DateField(default=datetime.now)
    subtotal=models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva=models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total=models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names
    
    class Meta:
        verbose_name='Venta'
        verbose_name_plural='Ventas'
        ordering=['id']

class DetSale(models.Model):
    sale=models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod=models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant=models.IntegerField(default=0)
    subtotal=models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name
    
    class Meta:
        verbose_name='Detalle de Venta'
        verbose_name_plural='Detalle de Ventas'
        ordering=['id']
