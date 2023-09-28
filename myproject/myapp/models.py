from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration = models.PositiveIntegerField()
    products = models.ManyToManyField(Product)

class UserLesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    viewed_time = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=[('Viewed', 'Viewed'), ('Not Viewed', 'Not Viewed')])