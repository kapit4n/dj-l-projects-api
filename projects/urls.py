from django.urls import path
from .views import ( 
    ProjectListApiView,
    ProjectDetailApiView
)

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/api", ProjectListApiView.as_view()),
    path("/api/<int:project_id>/", ProjectDetailApiView.as_view())
]
