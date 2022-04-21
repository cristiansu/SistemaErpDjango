from django.urls import path, include
from App.login.views import LoginFormView, LogoutView, LogoutRedirectView

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout'), #si no indicamos next page debemos indicar el logout_redirect_url
    path('logout/', LogoutRedirectView.as_view(), name='logout'),

]