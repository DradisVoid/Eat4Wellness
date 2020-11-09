from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Coach)
admin.site.register(Member)
admin.site.register(Nutrient)
admin.site.register(Ingredient)
admin.site.register(FoodProduct)
admin.site.register(Meal)
admin.site.register(FoodNutrient)
admin.site.register(HealthProfileNutrient)
admin.site.register(HealthProfile)
admin.site.register(MealFood)
