from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('diploma/', views.diploma, name='diploma'),
]