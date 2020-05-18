from django.urls import path
from django.contrib import admin
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.list_view, name='list_view'),
    path('<int:id>', views.perfil, name = 'perfil'),
    path('create_view', views.signup, name='create_view'),
]
