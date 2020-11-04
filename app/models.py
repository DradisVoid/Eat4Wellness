from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Member(User):
    member_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    coach = models.ForeignKey('Coach', on_delete=models.RESTRICT)


class Coach(User):
    coach_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)


class Admin(User):
    admin_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)


class Nutrient(models.Model):
    nutrient_name = models.CharField(max_length=50)


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)


class HealthProfile(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=1, choices=SEX)
    member = models.OneToOneField(Member, related_name='health_profile_of', on_delete=models.CASCADE)
    recommended_daily_nutrients = models.ManyToManyField(Nutrient, through='HealthProfileNutrient')
    average_daily_nutrients = models.ManyToManyField(Nutrient, through='HealthProfileNutrient')


class FoodProduct(models.Model):
    product_name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)
    nutrients = models.ManyToManyField(Nutrient, through='FoodNutrient')


class Meal(models.Model):
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    food_products = models.ManyToManyField(FoodProduct, through='MealFood')
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['-timestamp']


class FoodNutrient(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    food_product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)


class HealthProfileNutrient(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    health_profile = models.ForeignKey(HealthProfile, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)


class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food_product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)
    servings = models.PositiveIntegerField()
