from django.shortcuts import render
from django.views import generic
from users.models import Member
from food.models import Meal, MealFoodServings


# Create your views here.
class MealListView(generic.ListView):
    model = Meal

    def get_queryset(self):
        member = Member.objects.get(user_id=self.request.user)
        return Meal.objects.filter(member_id=member)


class MealDetailView(generic.DetailView):
    model = Meal


class MealItemDetailView(generic.DetailView):
    model = MealFoodServings


def food_compare(request):
    context = {}

    return render(request, 'member_food_compare.html', context=context)


def member_nutrition(request):
    member = Member.objects.get(user_id=request.user)
    meal_list = Meal.objects.filter(member_id=member)

    context = {
        'meal_list': meal_list
    }

    return render(request, 'member_nutrition.html', context=context)
