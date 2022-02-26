from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import recipes.models as models
from .forms import RecipeForm, ProductAmountForm
from django.forms.formsets import formset_factory, BaseFormSet


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


@login_required()
def add_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)

        ProductAmountFormset = formset_factory(ProductAmountForm, formset=BaseFormSet)
        product_amount_formset = ProductAmountFormset(request.POST)

        if recipe_form.is_valid() and product_amount_formset.is_valid():
            recipe = models.Recipe.objects.create()
            recipe.name = recipe_form.cleaned_data['name']
            recipe.description = recipe_form.cleaned_data['description']
            recipe.owner = request.user
            for product_amount in product_amount_formset:
                db_object = product_amount.save()
                recipe.ingredients.add(db_object.id)
            recipe.save()
            return redirect('recipes:home')
    else:
        recipe_form = RecipeForm()
        ProductAmountFormset = formset_factory(ProductAmountForm, formset=BaseFormSet)
        product_amount_formset = ProductAmountFormset()
    return render(request, 'add_recipe.html', {'recipe_form': recipe_form, 'product_amount_formset': product_amount_formset})