from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Member(User):
    member_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    coach = models.ForeignKey('Coach', on_delete=models.RESTRICT)

    def __str__(self):
        return self.member_name


class Coach(User):
    coach_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.coach_name


class Admin(User):
    admin_name = models.CharField(max_length=50)

    def __str__(self):
        return self.admin_name


class Nutrient(models.Model):
    nutrient_name = models.CharField(max_length=50)

    def __str__(self):
        return self.nutrient_name


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)

    def __str__(self):
        return self.ingredient_name


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

    def __str__(self):
        return str(self.member) + " Health Profile"


class FoodProduct(models.Model):
    product_name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Ingredient)
    nutrients = models.ManyToManyField(Nutrient, through='FoodNutrient')

    def __str__(self):
        return self.product_name


class Meal(models.Model):
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    food_products = models.ManyToManyField(FoodProduct, through='MealFood')
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.timestamp)


class FoodNutrient(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    food_product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nutrient) + " (" + str(self.amount) + " " + self.unit + ") - Food Product"


class HealthProfileNutrient(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    health_profile = models.ForeignKey(HealthProfile, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nutrient) + " (" + str(self.amount) + " " + self.unit + ") - Health Profile"


class MealFood(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    food_product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)
    servings = models.PositiveIntegerField()

    def __str__(self):
        return str(self.food_product) + " - " + str(self.servings) + " servings"
