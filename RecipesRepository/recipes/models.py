from django.db import models


class Product(models.Model):
    TYPE_CHOICES = [("Vegetable", "Vegetable"),
                    ("Fruit", "Fruit"),
                    ("Meat", "Meat"),
                    ("Spice", "Spice"),
                    ("Dairy", "Dairy"),
                    ("Bread", "Bread"),
                    ("Other", "Other")
                    ]
    KCAL_UNIT_CHOICES = [("100", "kcal/100g"), ("10", "kcal/10g"), ("1", "kcal/1g")]

    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    kcal_unit = models.CharField(max_length=20, choices=KCAL_UNIT_CHOICES)
    kcal = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
