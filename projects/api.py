from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet): #ViewSet es una clase que proporciona una interfaz simplificada para realizar operaciones CRUD 
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny] #Cualquier cliente puede solicitar datos de mi aplicacion
    serializer_class =  ProjectSerializer