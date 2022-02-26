from django.urls import path
import recipes.views as views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:recipe_id>', views.get_recipe, name='get_recipe'),
    path('add_recipe', views.add_recipe, name='add_recipe')
]