from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def home(request):
    return render(request, 'home.html')

# Carreras universitarias
def carreras(request):
    carreras = Carrera.objects.all()

    new_carrera = None
    if request.method == 'POST':
        carreras_form = CarreraForm(data=request.POST)
        if carreras_form.is_valid():
            new_carrera = carreras_form.save()
            new_carrera.save()
            return redirect(request.path)
    else:
        carreras_form = CarreraForm()

    return render(request, 'carreras.html', {'carreras': carreras, 'new_carrera': new_carrera,'carreras_form': carreras_form})

def eliminacionCarrera(request, carrera_id):
    carrera = Carrera.objects.get(codigo=carrera_id)
    carrera.delete()
    return redirect('App_matricula:carreras')

def edicionCarrera(request, carrera_id):
    carrera = Carrera.objects.get(codigo=carrera_id)
    return render(request, 'edicionCarrera.html', {'carrera':carrera})

def editarCarrera(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    duracion = request.POST['txtDuracion']
    carrera = Carrera.objects.get(codigo=codigo)
    carrera.nombre = nombre
    carrera.duracion = duracion
    carrera.save()
    return redirect('App_matricula:carreras')

# Cursos universitarios
def cursos(request):
    cursos = Curso.objects.all()
    
    new_curso = None
    if request.method == 'POST':
        cursos_form = CursoForm(data=request.POST)
        if cursos_form.is_valid():
            new_curso = cursos_form.save()
            new_curso.save()
            return redirect(request.path)
    else:
        cursos_form = CursoForm()
    
    return render(request, 'cursos.html', {'cursos': cursos, 'new_curso': new_curso, 'cursos_form': cursos_form})

def eliminacionCurso(request, curso_id):
    curso = Curso.objects.get(codigo=curso_id)
    curso.delete()
    return redirect('App_matricula:cursos')

def edicionCurso(request, curso_id):
    curso = Curso.objects.get(codigo=curso_id)
    return render(request, 'edicionCurso.html', {'curso': curso})

def editarCurso(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['txtCreditos']
    docente = request.POST['txtDocente']
    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.docente = docente
    curso.save()
    return redirect('App_matricula:cursos')

# Estudiantes universitarios
def estudiantes(request):
    estudiantes = Estudiante.objects.all()

    new_estudiante = None
    if request.method == 'POST':
        estudiantes_form = EstudianteForm(data=request.POST)
        if estudiantes_form.is_valid():
            new_estudiante = estudiantes_form.save()
            new_estudiante.save()
            return redirect(request.path)
    else:
        estudiantes_form = EstudianteForm()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes, 'new_estudiante': new_estudiante, 'estudiantes_form': estudiantes_form})

def eliminacionEstudiante(request, estudiante_dni):
    estudiante = Estudiante.objects.get(dni=estudiante_dni)
    estudiante.delete()
    return redirect('App_matricula:estudiantes')

def edicionEstudiante(request, estudiante_dni):
    # estudiante = Estudiante.objects.get(dni=estudiante_dni)
    # return render(request, 'edicionEstudiante.html', {'estudiante': estudiante})

    # estudiante = Estudiante.objects.get(dni=estudiante_dni)
    # formulario_estudiante = EstudianteForm(request.POST, instance=estudiante)
    # if formulario_estudiante.is_valid():
    #     formulario_estudiante.save()
    # return render(request, 'edicionEstudiante.html', {'estudiante': estudiante, 'formulario_estudiante': formulario_estudiante})

    # estudiante = get_object_or_404(Estudiante, dni=estudiante_dni) # Cuando no se trabaja con model from se realiza con este método
    estudiante = Estudiante.objects.get(dni=estudiante_dni)
    # formulario_estudiante = EstudianteForm(initial={'dni':estudiante.dni, 'apellidoPaterno':estudiante.apellidoPaterno, 'apellidoMaterno':estudiante.apellidoMaterno, 'nombres':estudiante.nombres, 'fechaNacimiento':estudiante.fechaNacimiento, 'sexo':estudiante.sexo, 'carrera':estudiante.carrera, 'vigencia':estudiante.vigencia})
    formulario_estudiante = EstudianteFormEdit(instance=estudiante)
    
    if request.method == 'POST':
        formulario_estudiante = EstudianteFormEdit(request.POST, instance=estudiante)
        if formulario_estudiante.is_valid():
            formulario_estudiante.save()
            return redirect('App_matricula:estudiantes')
    return render(request, 'edicionEstudiante.html', {'estudiante': estudiante,'formulario_estudiante': formulario_estudiante})

# Matrículas
def matriculas(request):
    matriculas = Matricula.objects.all()

    new_matricula = None
    if request.method == 'POST':
        matricula_form = MatriculaForm(data=request.POST)
        if matricula_form.is_valid():
            new_matricula = matricula_form.save()
            new_matricula.save()
            return redirect('App_matricula:matriculas')
    else:
        matricula_form = MatriculaForm()
    context = {'matriculas': matriculas, 'new_matricula': new_matricula, 'matricula_form': matricula_form}
    return render(request, 'matricula.html', context)

def eliminacionMatricula(request, matricula_id):
    matricula = Matricula.objects.get(id=matricula_id)
    matricula.delete()
    return redirect('App_matricula:matriculas')