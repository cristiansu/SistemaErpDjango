from dataclasses import fields
from tkinter import Widget
from turtle import textinput
from django import forms
from django.forms import ModelForm, TextInput, Textarea
from App.erp.models import Category, Product, Client
from django.forms import *
from datetime import datetime

class CategoryForm(ModelForm):

    #otra forma con la sobre escritura del método init
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():              ----se comenta para usar la librería django-widget-tweaks q permite agregar clases en html
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True
            

    class Meta:
        model = Category
        fields = '__all__'
        # labels = {               #no es necesario usar labels pq en el modelo se indicó el verbose_name que actua como label
        #     'name': 'Nombre',
        #     'desc': 'Descripción'
        # }
        widgets = {
            'name': TextInput(
                attrs={
                    #'class':'form-control',
                    'placeholder':'Ingrese nombre de la categoría',
                    #'autocomplete': 'off'
                }
            ),
            'desc': Textarea(
                attrs={
                    #'class':'form-control',
                    'placeholder':'Ingrese descripción de la categoría',
                    #'autocomplete': 'off',
                    'rows':3,
                    'cols':3
                }
            )
            
        }
        exclude = ['user_creation', 'user_updated'] #se utiliza para no mostrar en formularios estos campos

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)

        return data


    # el método clean se usa para controlar errores q no tienen relación directa con un campo de la base de datos. por ejemplo la cantidad
    # de caracteres q básicamente si es de 1 o 2 o más caracteres para el modelo no sería problema, pero si sería importante de haber 
    # alguna necesidad de controlarlo
    #---para probar se debe verificar estar en la url correcta, es decir la del formView
    def clean(self):
        cleaned = super().clean() #esta variable cleaned arroja un diccionario con los componentes del formulario, es decir se puede acceder a ellos
        if len(cleaned['name']) <= 2:
            #self.add_error('name', 'No cumple mínimo de caracteres')
            #----para cuando se quieren controlar errores q no tienen relación alguna con los componentes del formulario 
            # se usa el método ValidationError antecedido por la palabra reservada 'raise'. además se debe ajustar el html para ver estos errores
            raise forms.ValidationError('Validación método clean category/forms.py')

        return cleaned


#-----------Form para productos ----------------------------
class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre del producto',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class TestForm(Form):
    
    categories = ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
        'class': 'form-control select2', #se agrega la clase select2 por requerimiento de la librería select2
        'style': 'width:100%'
    }))

    products = ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width:100%'
    }))
    

class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus nombres',
                }
            ),
            'surnames': TextInput(
                attrs={
                    'placeholder': 'Ingrese sus apellidos',
                }
            ),
            'dni': TextInput(
                attrs={
                    'placeholder': 'Ingrese su rut',
                }
            ),
            'date_birthday': DateInput(format='%Y-%m-%d',
                attrs={
                    'value': datetime.now().strftime('%Y-%m-%d'),
                }
            ),
            'address': TextInput(
                attrs={
                    'placeholder': 'Ingrese su dirección',
                }
            ),
            'gender': Select()
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data