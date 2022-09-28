from django import forms
from .models import *

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        # fields = ['nombre', 'duracion']
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'duracion': 'Duración'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'creditos', 'docente']
        labels = {
            'nombre': 'Curso',
            'creditos': 'Créditos',
            'docente': 'Docente'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'creditos': forms.NumberInput(attrs={'class': 'form-control'}),
            'docente': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['dni', 'apellidoPaterno', 'apellidoMaterno', 'nombres', 'fechaNacimiento', 'sexo', 'carrera', 'vigencia']
        labels = {
            'dni': 'DNI',
            'apellidoPaterno': 'Apellido Paterno',
            'apellidoMaterno': 'Apellido Materno',
            'nombres': 'Nombres',
            'fechaNacimiento': 'Fecha de nacimiento',
            'sexo': 'Sexo',
            'carrera': 'Carrera',
            'vigencia': 'Activo'
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DNI'}),
            'apellidoPaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoMaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaNacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 2022-08-29'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'vigencia': forms.CheckboxInput(attrs={'class': 'form-check form-check-input'}),
        }

class EstudianteFormEdit(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['dni', 'apellidoPaterno', 'apellidoMaterno', 'nombres', 'fechaNacimiento', 'sexo', 'carrera', 'vigencia']
        labels = {
            'dni': 'DNI',
            'apellidoPaterno': 'Apellido Paterno',
            'apellidoMaterno': 'Apellido Materno',
            'nombres': 'Nombres',
            'fechaNacimiento': 'Fecha de nacimiento',
            'sexo': 'Sexo',
            'carrera': 'Carrera',
            'vigencia': 'Vigencia'
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'apellidoPaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoMaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaNacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Ejemplo: 2022-08-29'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'vigencia': forms.CheckboxInput(attrs={'class': 'form-check form-check-input'}),
        }

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['estudiante', 'curso']
        labels = {
            'estudiante': 'Estudiante',
            'curso': 'Curso'
        }
        widgets = {
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
        }