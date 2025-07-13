from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_quantity/', views.update_quantity, name='update_quantity'),

    path('dashboard/', views.dashboard, name='dashboard'),  

]
