from django.urls import path

from . import views

app_name = 'comments'

urlpatterns = [
    path('post/<int:post_id>/comentar/', views.add_comment, name='add_comment'),
]