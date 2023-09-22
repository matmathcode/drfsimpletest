from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter() #funcion de django rest que permite definir las rutas URL para tus vistas basadas en clases

router.register('api/projects', ProjectViewSet, 'projects') # registro una ruta llamada api/projects

urlpatterns = router.urls #ahora las rutas forman parte de la aplicacion