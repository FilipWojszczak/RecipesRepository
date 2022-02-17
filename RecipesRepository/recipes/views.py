from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import recipes.models as models


def home(request):
    if request.user.is_authenticated:
        owned_recipes = request.user.owned_recipes
        return render(request, 'home_logged.html', {'owned_recipes': owned_recipes})
    else:
        return render(request, 'home.html')


@login_required()
def get_recipe(request, recipe_id):
    try:
        recipe = models.Recipe.objects.get(pk=recipe_id)
        if recipe in request.user.owned_recipes.all():
            return render(request, 'get_recipe.html', {'recipe': recipe})
        else:
            return render(request, 'error.html')
    except models.Recipe.DoesNotExist:
        return render(request, 'error.html')
