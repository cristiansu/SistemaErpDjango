from re import template
import re
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import RedirectView

# Create your views here.

class LoginFormView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        #print(request.user) permite ver quién es el usuario logeado
        if request.user.is_authenticated: #causará q aunque retorne a la url de login, se redirigirá automáticamente a category_list
            #return redirect('erp:category_list')
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context

#para cerrar la sesión no es necesario crear una vista basada en clase o función, basta con importar LogoutView y citarla directo desde las urls

class LogoutRedirectView(RedirectView):
    pattern_name = 'login'

    #esta vista por defecto redirecciona pero no cierra sesión. para ello usaremos dispach y la función logout con el request como parámetro
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)