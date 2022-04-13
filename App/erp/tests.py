from django.test import TestCase

# Create your tests here.

# Create your tests here.
from Proyecto.wsgi import *
from App.erp.models import *

data = ['Bebidas','Lácteos','Frutas','Verduras','Conservas','Congelados','Fideos']

for i in data:
    cat = Category(name=i)
    cat.save()
    print('Guardado registro N°{}'.format(cat.id))
