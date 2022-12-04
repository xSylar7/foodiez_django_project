from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()


class Recipies (models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'recipies')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= 'recipies')