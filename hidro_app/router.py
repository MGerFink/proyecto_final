from rest_framework import routers
from .viewsets import UsuarioViewSet

router = routers.SimpleRouter()
router.register("api-usuario",UsuarioViewSet)