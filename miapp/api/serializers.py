from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from miapp.models import *

class ApiSerilizer(ModelSerializer):
    nombre_profesor = serializers.CharField(source='profesor.nombre', read_only=True)
    nombre_asignatura = serializers.CharField(source='Asignaturas.nombreasignatura', read_only=True)
    nombre_asignatura = serializers.CharField(source='Asignaturas.nombreasignatura', read_only=True)
    class Meta:
      model = Clases
      fields = '__all__'    
class AsistenciaSerilizer(ModelSerializer):   
    nombre_alumno = serializers.CharField(source='alumnos.nombre', read_only=True) 
    apellido_alumno = serializers.CharField(source='alumnos.apellido', read_only=True)    
    class Meta:
      model = Asistencia
      fields = '__all__'        