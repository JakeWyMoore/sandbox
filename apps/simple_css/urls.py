from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('buttons', views.buttons),
    path('color-schemes', views.color_schemes),

]