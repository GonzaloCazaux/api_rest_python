from django.db import models

class Asignaturas(models.Model):
    asignaturaid = models.AutoField(primary_key=True)
    nombreasignatura = models.CharField(max_length=100)
    descripcionasignatura = models.TextField()

class Alumnos(models.Model):
    alumnoid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correoelectronico = models.EmailField()
    telefono = models.CharField(max_length=15)

class Profesores(models.Model):
    profesorid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correoelectronico = models.EmailField()
    telefono = models.CharField(max_length=15)

class Clases(models.Model):
    claseid = models.AutoField(primary_key=True)
    profesor = models.ForeignKey(Profesores, on_delete=models.CASCADE)
    Asignaturas = models.ForeignKey(Asignaturas, on_delete=models.CASCADE)
    horario = models.CharField(max_length=50)
    fecha_clase = models.DateField()
    aula = models.CharField(max_length=50)

class Asistencia(models.Model):
    asistenciaid = models.AutoField(primary_key=True)
    alumnos = models.ForeignKey(Alumnos, on_delete=models.CASCADE)
    clases = models.ForeignKey(Clases, on_delete=models.CASCADE)
    fechaasistencia = models.DateField()
    estadoasistencia = models.CharField(max_length=20)
