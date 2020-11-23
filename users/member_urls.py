"""
App specific urls
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='member_homepage'),
    path('add_meal/', views.meal_add, name='member_add_meal'),
    path('compare_food/', views.food_compare, name='member_compare_meal'),
    path('meals/', views.MealListView.as_view(), name='member_meals'),
    path('meals/<int:pk>', views.MealDetailView.as_view(), name='meal-detail-view'),
    path('meals/foodproducts/<int:pk>', views.FoodProductDetailView.as_view(), name='food-product-detail-view'),
]
