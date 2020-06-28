from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(default='def.png', blank=True)
    body = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True,
            blank=True, null=True)

photo = models.ImageField(upload_to="gallery")