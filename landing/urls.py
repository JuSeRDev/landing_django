from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('diploma/', views.diploma, name='diploma'),
    path('gestor/', views.gestor, name='gestor'),
    path('cv/', views.cv, name='cv')
]