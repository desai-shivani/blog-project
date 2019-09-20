from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserPost(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=128)
    def __str__(self):
        return self.title