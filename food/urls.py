"""
App specific urls
"""

from django.urls import path
from . import views

urlpatterns = [
    path('meals/', views.MealListView.as_view(), name='member_meals'),
    path('meals/<int:pk>', views.MealDetailView.as_view(), name='meal-detail-view'),
    path('meals/item/<int:pk>', views.MealItemDetailView.as_view(), name='meal-item-detail-view'),
    path('compare/', views.food_compare, name='member_compare_food'),
    path('nutrition/', views.member_nutrition, name='member_nutrition'),
]
