from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.
def cursos(request):
    curso = Curso(nombre="Python", camada=1000)
    curso.save()
    return HttpResponse(f"Se creo el curso {curso.nombre} ")

def inicio(request):
    return HttpResponse("Vista Inicio")

def profesores(request):
    return render(request, "AppCoder/profesores.html")
    
def estudiantes(request):
    return HttpResponse("Vista Estudiantes")

def entregables(request):
    return HttpResponse("Vista Entregables")