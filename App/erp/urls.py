from django.contrib import admin
from django.urls import path, include
from App.erp.views.category.views import *
from App.erp.views.product.views import *
from App.erp.views.dashboard.views import *
from App.erp.views.test.views import TestView
from App.erp.views.client.views import ClientView


app_name = 'erp'

urlpatterns = [
    #category
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDelete.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
    #home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # product
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    #test select anidados
    path('test/', TestView.as_view(), name='test'),
    # client
    path('client/', ClientView.as_view(), name='client'),    

    
    
    
]