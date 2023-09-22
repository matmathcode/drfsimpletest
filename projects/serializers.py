from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer): #Convierte  un modelo en datos que pueden ser consultados
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at', )
        read_only_fields = ('created_at', ) #Es un campo solo para leer y no se puede actualizar