from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home, name='home'),
    path('criar-post/', views.create_post, name='create_post'),
    path('meus-posts/', views.my_posts, name='my_posts'),
    path('editar-post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('enviar-para-analise/<int:post_id>/', views.send_to_review, name='send_to_review'),
    path('editorial/', views.editorial_list, name='editorial_list'),
    path('editorial/<int:post_id>/', views.editorial_detail, name='editorial_detail'),
    path('editorial/<int:post_id>/aprovar/', views.approve_post, name='approve_post'),
    path('editorial/<int:post_id>/rejeitar/', views.reject_post, name='reject_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]