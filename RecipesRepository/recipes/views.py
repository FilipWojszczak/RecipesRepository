from django.shortcuts import render
# from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        owned_recipes = request.user.owned_recipes
        return render(request, 'home_logged.html', {'owned_recipes': owned_recipes})
    else:
        return render(request, 'home.html')
