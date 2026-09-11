from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('cadastro/', views.signup, name='signup'),
    path('entrar/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/editar/', views.edit_profile, name='edit_profile'),
    path('@<str:username>/', views.profile, name='profile'),
]