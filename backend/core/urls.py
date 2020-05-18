from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'core'

urlpatterns = [
  path('', views.index, name='index'),
  path('info', views.info, name='info'),
  path('info_statistic', views.info_statistic, name='info_statistic'),
  path('diagnostico/', views.DiagnosticoView.as_view(template_name='core/result.html'), name='result'),
  path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name="login"),
  path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name="logout"),
]
