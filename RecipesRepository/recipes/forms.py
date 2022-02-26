from django import forms
from .models import Recipe, ProductAmount, Product


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description')


class ProductAmountForm(forms.ModelForm):
    # product = forms.CharField() # TODO change widget for product for charfield with hints

    class Meta:
        model = ProductAmount
        exclude = []

    # def save(self, commit=True):
    #     product = Product.objects.get(name=self.cleaned_data['product'])
    #     self.cleaned_data['product'] = product.id
    #     return super(ProductAmountForm, self).save(commit)
