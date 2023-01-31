from django.urls import path
from AppCoder import views

urlpatterns = [
    path('cursos/', views.cursos),
    path('', views.inicio),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables),    
]