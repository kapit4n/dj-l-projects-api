from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500)
    dir = models.CharField(max_length = 200)
    img = models.CharField(max_length = 250)
    size = models.IntegerField(blank=True, null=True)
    contributions = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    language = models.CharField(max_length = 100)
    languages = models.CharField(max_length = 500)
    skills = models.CharField(max_length = 500,  blank=True, null=True)
    features = models.CharField(max_length = 500)
    categories = models.CharField(max_length = 500, blank=True, null=True)

    def __str__(self):
        return self.name
