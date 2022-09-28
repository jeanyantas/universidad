from django.db import models

class Carrera(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)
    def __str__(self):
        return f"{self.nombre} (Duración: {self.duracion} año(s))"

class Curso(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre} ({self.codigo}) / Docente: {self.docente}"

class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices = sexos, default='F')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)
    def nombreCompleto(self):
        return f"{self.apellidoPaterno} {self.apellidoMaterno}, {self.nombres}"
    def __str__(self):
        if self.vigencia:
            estadoEstudiante = "VIGENTE"
        else:
            estadoEstudiante = "DE BAJA"
        return f"{self.nombreCompleto()} / Carrera: {self.carrera} / {estadoEstudiante}"

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        if self.estudiante.sexo == 'F':
            letraSexo = 'a'
        else:
            letraSexo = 'o'
        fecMat = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return f"{self.estudiante.nombreCompleto()} matriculad{letraSexo} en el curso {self.curso} / Fecha: {fecMat}"