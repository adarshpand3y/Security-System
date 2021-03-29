from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('handleLogin', views.handleLogin),
    path('handleLogout', views.handleLogout),
    path('handleRegister', views.handleRegister),
    path('dashboard', views.dashboard),
]
