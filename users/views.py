import sys

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from users.models import *
from users.forms import *
from food import models as food_models
from search import api_calls


# Create your views here.
def homepage(request):
    context = {}

    return render(request, 'homepage.html', context=context)


# Admin pages
def admin_analytics(request):
    context = {}

    return render(request, 'admin_analytics.html', context=context)


def admin_add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            if user.is_member:
                member = Member(user=user, coach_id=form.cleaned_data.get('coach_id'))
                member.save()
            if user.is_coach:
                coach = Coach(user=user)
                coach.save()
            if user.is_admin:
                user.is_staff = True
                user.save()
                admin = Admin(user=user)
                admin.save()

            return HttpResponseRedirect(reverse('admin_add_user') + '?s=1')
    else:
        form = AddUserForm()

    context = {
        'form': form,
        's': request.GET.get('s', '0')
               }
    return render(request, 'admin_add_user.html', context=context)


# Coach pages


# Member pages
def meal_add(request):
    if request.method == 'POST':
        form = AddMealForm(request.POST)
        if form.is_valid():
            timestamp = form.cleaned_data.get('date')
            member = Member.objects.get(user=request.user)

            meal = food_models.Meal(member_id=member.id, timestamp=timestamp)
            meal.save()

            food_list_text = form.cleaned_data.get('food_list')
            food_list = food_list_text.split(",")

            for food_id in food_list:
                if food_id == '':
                    continue

                food_data = api_calls.get_food(food_id)
                name = food_data.get('name')

                food_product, created = food_models.FoodProduct.objects.get_or_create(
                    product_name=name,
                    fdc_id=food_id
                )

                print(name + str(created), file=sys.stderr)

                if created:
                    # foodproduct not already in db
                    ingredients = food_data.get('ingredients')

                    print(ingredients, file=sys.stderr)

                    for ingr_key in ingredients:
                        ingredient = ingredients.get(ingr_key)
                        ingr_name = ingredient.get('name')

                        ingredient_obj, ingr_created = food_models.Ingredient.objects.get_or_create(
                            ingredient_name=ingr_name
                        )

                        food_product.ingredients.add(ingredient_obj)

                    nutrients = food_data.get('nutrients')

                    print(nutrients, file=sys.stderr)

                    for nutr_key in nutrients:
                        nutrient = nutrients.get(nutr_key)
                        nutr_name = nutrient.get('name')
                        nutr_unit = nutrient.get('unit')
                        nutr_amount = nutrient.get('amount')

                        nutr_obj, nutr_created = food_models.Nutrient.objects.get_or_create(
                            nutrient_name=nutr_name
                        )

                        nutr_through = food_models.FoodNutrient.objects.create(
                            nutrient=nutr_obj, food_product=food_product, amount=nutr_amount, unit=nutr_unit
                        )

                    food_product.save()

                meal.food_products.add(food_product)

            meal.save()

            return HttpResponseRedirect(reverse('member_add_meal') + '?s=1')

    else:
        form = AddMealForm()

    context = {
        'form': form
    }

    return render(request, 'member_meal_add.html', context=context)


def food_compare(request):
    context = {}

    return render(request, 'member_food_compare.html', context=context)
