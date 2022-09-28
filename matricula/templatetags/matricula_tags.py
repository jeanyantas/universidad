from django import template
from ..models import Carrera, Curso, Estudiante

register = template.Library()

@register.simple_tag
def total_carreras():
    carreras = len(Carrera.objects.all())
    return carreras

@register.simple_tag
def total_cursos():
    cursos = len(Curso.objects.all())
    return cursos

@register.simple_tag
def total_estudiantes():
    estudiantes = len(Estudiante.objects.all())
    return estudiantes

@register.simple_tag
def total_estudiantes_activos():
    estudiantes = len(Estudiante.objects.filter(vigencia=True))
    return estudiantes