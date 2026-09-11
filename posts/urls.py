from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('criar-post/', views.create_post, name='create_post'),
    path('meus-posts/', views.my_posts, name='my_posts'),
    path('editar-post/<int:post_id>/', views.edit_post, name='edit_post'),
]