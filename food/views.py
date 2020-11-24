import sys
from django.shortcuts import render
from django.views import generic
from users.models import Member
from food.models import Meal, MealFoodServings
from datetime import datetime, timedelta


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

    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    meal_list = Meal.objects.filter(member_id=member, timestamp__range=(start_date, end_date))

    date_set = set()
    nutrient_set = {}

    # get number of days
    for meal in meal_list:
        meal_date = meal.timestamp
        date = datetime(year=meal_date.year, month=meal_date.month, day=meal_date.day)
        date_set.add(date)

        for food_product in meal.food_products.all():
            for nutrient in food_product.foodnutrient_set.all():
                if nutrient.nutrient.nutrient_name in nutrient_set:
                    nutrient_set[nutrient.nutrient.nutrient_name]['amount'] += nutrient.amount
                else:
                    nutrient_set[nutrient.nutrient.nutrient_name] = {
                        'amount': nutrient.amount,
                        'unit': nutrient.unit
                    }

    num_days = len(date_set)
    unsorted_nutrient_list = []
    for nutrient in nutrient_set:
        unsorted_nutrient_list.append({
            'name': nutrient,
            'amount': round(nutrient_set.get(nutrient).get('amount') / num_days, 2),
            'unit': nutrient_set[nutrient].get('unit')
        })

    sorted_nutrient_list = sorted(unsorted_nutrient_list, key=lambda k: k['name'], reverse=True)

    context = {
        'nutrient_list': sorted_nutrient_list
    }

    return render(request, 'member_nutrition.html', context=context)
