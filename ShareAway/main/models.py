from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Idea(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return(f"{self.title}, Author: {self.author}")