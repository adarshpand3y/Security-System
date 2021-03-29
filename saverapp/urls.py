from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('handleLogin', views.handleLogin),
    path('handleLogout', views.handleLogout),
    path('handleRegister', views.handleSignup),
    path('dashboard', views.dashboard),
    path('checkuser', views.check_username),
    path('submitreport', views.submit_report),
]
