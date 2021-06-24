from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('login-logic', views.login_logic),
    path('reg-logic', views.reg_logic),
    path('logout', views.logout),
    path('add-image', views.add_image),
    path('delete/<int:img_id>', views.delete),
]