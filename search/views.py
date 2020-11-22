from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Get API key from file
from .api_key import API_KEY


# Create your views here.
@csrf_exempt
def search_food(request):
    if request.method == 'POST':

        url = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=' + API_KEY

        query = request.POST['s']

        data = {
            "query": query,
            "dataType": [
                "Survey (FNDDS)"
            ]
        }

        r = requests.post(url, json=data)

        json_data = r.json()

        response = {}

        if json_data["totalHits"] > 0:
            count = 0
            for item in json_data['foods']:
                response[item['fdcId']] = {
                    'name': item['description']
                }
                count += 1

        return JsonResponse(response)
    else:
        return JsonResponse({})


@csrf_exempt
def get_nutrients(request):
    if request.method == 'POST':

        food_id = request.POST['id']

        url = f'https://api.nal.usda.gov/fdc/v1/food/{food_id}?api_key=' + API_KEY

        r = requests.get(url)

        json_data = r.json()

        ingr_list = {}
        count_i = 0
        for item in json_data['inputFoods']:
            try:
                ingr_list[count_i] = {'name': item['ingredientDescription']}
                count_i += 1
            except:
                pass

        nutr_list = {}
        count_n = 0
        for item in json_data['foodNutrients']:
            try:
                nutr_list[count_n] = {
                    'name': item['nutrient']['name'],
                    'unit': item['nutrient']['unitName'],
                    'amount': item['amount']
                }
                count_n += 1
            except:
                pass

        return JsonResponse({
            'ingredients': ingr_list,
            'nutrients': nutr_list
        })
    else:
        return JsonResponse("")
