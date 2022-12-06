from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView

from backend.serializers import CategoryListSerializer, RecipeDetailSerializer, RecipeListSerializer
from .models import Ingredient, Recipe, Category
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
# Create your views here.
class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes=[AllowAny]

# class CategoryDetailedView(RetrieveAPIView):
#     queryset=Recipe.objects.all()
#     serializer_class= RecipeDetailSerializer
#     lookup_field= 'category'
#     lookup_url_kwarg='category_id'
#     permission_classes=[AllowAny]

class RecipeListView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer
    permission_classes=[AllowAny]


class RecipeDetailedView(RetrieveAPIView):
    queryset=Recipe.objects.all()
    serializer_class= RecipeDetailSerializer
    lookup_field= 'id'
    lookup_url_kwarg='recipe_id'
    permission_classes=[AllowAny]


# class RecipeUpdateView(RetrieveUpdateAPIView):
#     queryset=Recipe.objects.all()
#     serializer_class=RecipeCreateSerializer
#     lookup_fields='id'
#     lookup_url_kwarg='recipe_id'
#     permission_classes=[IsAuthenticated, IsAdminUser]

# class RecipeDeleteView(DestroyAPIView): 
#     queryset = Recipe.objects.all()
#     serializer_class =RecipeListSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'recipe_id'
#     permission_classes=[IsAuthenticated, IsAdminUser,]

# class RecipeCreateAPIview(CreateAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class= RecipeCreateSerializer
#     permission_classes=[AllowAny]
#     lookup_field = 'id'
#     lookup_url_kwarg = 'recipe_id'
    
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user, recipe=Recipe.objects.get(id=self.kwargs["recipe_id"]))
