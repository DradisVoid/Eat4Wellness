from django.shortcuts import reverse
from django.db import models
from users.models import Member


# Create your models here.
class Nutrient(models.Model):
    nutrient_name = models.CharField(max_length=50)

    def __str__(self):
        return self.nutrient_name


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredient_name


class FoodProduct(models.Model):
    product_name = models.CharField(max_length=50)
    fdc_id = models.PositiveIntegerField(unique=True, null=True)
    ingredients = models.ManyToManyField(Ingredient)
    nutrients = models.ManyToManyField(Nutrient, through='FoodNutrient')

    def __str__(self):
        return self.product_name


class Meal(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    food_products = models.ManyToManyField(FoodProduct, through='MealFoodServings')
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.timestamp)

    def get_absolute_url(self):
        return reverse('meal-detail-view', args=[str(self.id)])


class FoodNutrient(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    food_product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nutrient) + " (" + str(self.amount) + " " + self.unit + ") - Food Product"


class FoodPortion(models.Model):
    description = models.CharField(max_length=255)
    gram_weight = models.PositiveIntegerField()

    def __str__(self):
        return self.description + " (" + str(self.gram_weight) + "g)"


class MealFoodServings(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food_product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)
    portion = models.ForeignKey(FoodPortion, on_delete=models.CASCADE)
    servings = models.PositiveIntegerField()

    def __str__(self):
        return str(self.food_product) + " (" + str(self.servings) + " servings)"

    def get_absolute_url(self):
        return reverse('meal-item-detail-view', args=[str(self.id)])

    def get_amount_ratio(self):
        # return ratio of actual amount (portion * servings) to 100 g used in nutrients
        return (self.portion.gram_weight * self.servings) / 100
