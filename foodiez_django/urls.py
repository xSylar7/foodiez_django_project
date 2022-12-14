
from django.contrib import admin
from django.urls import path
from users.views import UserCreateAPIView, UserLoginAPIView, MyTokenObtainPairView
from backend import views as backend_views
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),

    path('categories/', backend_views.CategoryListView.as_view(), name = "categories"),
    path('categories/add/', backend_views.CategoryCreateAPIview.as_view(), name = "create-category"),
    path('recipes/', backend_views.RecipeListView.as_view(), name= "recipes"), 
    path('recipes/<int:recipe_id>/', backend_views.RecipeDetailedView.as_view()),
    path('recipes/add/', backend_views.RecipeCreateAPIview.as_view(), name='create-recipe'), 
    
    
]

#path('recipes/add/', backend_views.RecipeCreateAPIview.as_view(), name='create-recipe'),



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)