#---------esta vista se usa para mostrar select anidados video 44-----------------
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import TemplateView

from App.erp.forms import TestForm
from App.erp.models import Product, Category


class TestView(TemplateView):
    template_name = 'test.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                #data = [] no se usará pq para select2 se debe entregar el vacio(-------) según formato
                data = [{'id':'', 'text': '----------------'}] #será el valor por defecto vacio requerido por select2
                for i in Product.objects.filter(cate_id=request.POST['id']):
                    #data.append({'id':i.id, 'name':i.name}) se comenta pq para usar select2 se debe indicar como text
                    data.append({'id':i.id, 'text':i.name, 'data':i.cate.toJSON()})
            elif action == 'autocomplete':
                data = []
                for i in Category.objects.filter(name__icontains=request.POST['term'])[0:10]: #term se define el el ajax del form.html
                    item = i.toJSON()
                    #item['value'] = i.name #se crea variable pq item es un diccionario con 2 claves level y value, sólo necesitamos value
                    item['text'] = i.name #se sobre escribre linea anterior para usar select2 que requiere text
                    data.append(item)    
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Anidados | Django'
        context['form'] = TestForm()
        return context