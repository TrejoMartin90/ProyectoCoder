from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.
def crearCurso(request):
    curso = Curso(nombre="Python", camada=1000)
    curso.save()
    return HttpResponse(f"Se creo el curso {curso.nombre} ")