from dataclasses import fields
from tkinter import Widget
from turtle import textinput
from django.forms import ModelForm, TextInput, Textarea
from App.erp.models import Category

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