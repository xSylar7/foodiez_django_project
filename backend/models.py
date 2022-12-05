from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name



class Recipe (models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'recipies')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name= 'recipies')
    ingredients=models.ManyToManyField('Ingredient', related_name= 'recipies')
    def __str__(self):
        return f"{self.user.username}: {self.name}"

class Ingredient (models.Model):
    name:models.CharField(max_length=60)
    category:models.ManyToManyField(Category, related_name= 'ingrdients')
    user:models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'ingredients')
    recipe:models.ManyToManyField(Recipe, related_name= 'ingredients')
    def __str__(self):
        return f"{self.name}: {self.category}"