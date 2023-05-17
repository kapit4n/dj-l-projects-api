from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "user", "dir", "contributions", "size", "description", "img", "languages", "skills", "created_at", "updated_at"]
