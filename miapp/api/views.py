from rest_framework.viewsets import ModelViewSet
from miapp.models import *
from miapp.api.serializers import *

class MiappApiViewSet(ModelViewSet):
    serializer_class = ApiSerilizer
    queryset = Clases.objects.all()

class AsistenciaApiViewSet(ModelViewSet):
    serializer_class = AsistenciaSerilizer
    queryset = Asistencia.objects.all()
