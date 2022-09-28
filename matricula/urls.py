from django.urls import path
from . import views

app_name = 'App_matricula'

urlpatterns = [
    path('', views.home, name='home'),

    # Carreras universitarias
    path('carreras', views.carreras, name='carreras'),
    path('eliminacionCarrera/<carrera_id>', views.eliminacionCarrera, name='eliminacionCarrera'),
    path('edicionCarrera/<carrera_id>', views.edicionCarrera, name='edicionCarrera'),
    path('editarCarrera/', views.editarCarrera, name='editarCarrera'),

    # Cursos universitarios
    path('cursos/', views.cursos, name='cursos'),
    path('<int:curso_id>', views.eliminacionCurso, name='eliminacionCurso'),
    path('edicionCurso/<int:curso_id>', views.edicionCurso, name='edicionCurso'),
    path('editarCurso/', views.editarCurso, name='editarCurso'),

    # Estudiantes universitarios
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('eliminacionEstudiante/<estudiante_dni>', views.eliminacionEstudiante, name='eliminacionEstudiante'),
    path('edicionEstudiante/<str:estudiante_dni>', views.edicionEstudiante, name='edicionEstudiante'),

    # Matrículas
    path('matriculas/', views.matriculas, name='matriculas'),
    path('eliminacionMatricula/<int:matricula_id>', views.eliminacionMatricula, name='eliminacionMatricula'),
]