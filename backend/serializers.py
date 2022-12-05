from rest_framework import serializers
from backend.models import Category, Recipe, Ingredient


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields=['id','name', 'image']

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model= Category 
        fields=['name','category','user','ingredient', 'image']


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields=['name','image',]


class RecipeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id','name', 'user', 'image', 'category']

# class RecipeDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Recipe
#         fields=['name','category','user','ingredient', 'image']

# class RecipeCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Recipe
#         fields=['name', 'user', 'category', 'ingredient']

# class CategoryCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Ingredient
#         fields=['name','category']