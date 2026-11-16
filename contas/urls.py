from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView, CadastroView

app_name = 'contas'

urlpatterns = [
    path('login/',CustomLoginView.as_view(), name = 'login'),
    path('cadastro/',CadastroView.as_view(), name = 'cadastro'),
    path('logout/',LogoutView.as_view(), name = 'logout'),    
]

