from django.urls import path

from . import views


urlpatterns = [
    # Главная страница
    path('', views.index),
    # Список мороженого
    path('posts/', views.group_posts),
]
