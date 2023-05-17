
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import UserViewSet

# ViewSets define the view behavior.

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path("projects/", include("projects.urls")),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
