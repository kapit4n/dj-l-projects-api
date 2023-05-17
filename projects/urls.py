from django.urls import path
from .views import ( 
    ProjectListApiView,
)

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/api", ProjectListApiView.as_view())
]
