from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('/dashboard', views.dashboard),
    path('/login-logic', views.login_logic),
    path('/reg-logic', views.reg_logic),
    path('/logout', views.logout)
]