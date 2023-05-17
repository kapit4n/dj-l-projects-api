from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Project
from .serializers import ProjectSerializer

class ProjectListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        projects = Project.objects.filter(user = request.user.id)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'dir': request.data.get('dir'),
            'contributions': request.data.get('contributions'),
            'size': request.data.get('size'),
            'languages': request.data.get('languages'),
            'skills': request.data.get('skills'),
            'language': request.data.get('language'),
            'features': request.data.get('features'),
            'categories': request.data.get('categories'),
            'img': request.data.get('img'),
            'user': request.user.id,
        }

        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, project_id, user_id):
        try:
            return Project.objects.get(id=project_id, user=user_id)
        except Project.DoesNotExist:
            return None
        
    def get(self, request, project_id, *args, **kwargs):
        project_instance = self.get_object(project_id, request.user.id)

        if not project_instance:
            return Response(
                {"res": "project does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = ProjectSerializer(project_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, project_id, *args, **kwargs):
        project_instance = self.get_object(project_id, request.user.id)

        if not project_instance:
            return Response(
                {"res": "project does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        project_instance.delete()

        serializer = ProjectSerializer(project_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.
def index(request):
    return HttpResponse("Hello world from projects api")

