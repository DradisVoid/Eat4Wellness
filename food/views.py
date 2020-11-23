from django.shortcuts import render
from django.views import generic
from users.models import Member
from food import models as food_models
from search import api_calls


# Create your views here.
class MealListView(generic.ListView):
    model = food_models.Meal

    def get_queryset(self):
        member = Member.objects.get(user_id=self.request.user)
        return food_models.Meal.objects.filter(member_id=member)


class MealDetailView(generic.DetailView):
    model = food_models.Meal


class FoodProductDetailView(generic.DetailView):
    model = food_models.FoodProduct
