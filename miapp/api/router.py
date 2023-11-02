from rest_framework.routers import DefaultRouter
from miapp.api.views import *

router_get = DefaultRouter()
router_get2 = DefaultRouter()
router_get.register(prefix='miapp', basename='post', viewset=MiappApiViewSet)
router_get2.register(prefix='miappAsistencia', basename='post', viewset=AsistenciaApiViewSet)



