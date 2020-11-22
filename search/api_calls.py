from django.shortcuts import render
import requests

# Get API key from file
from .api_key import API_KEY


def get_food(fdcId):
    url = f'https://api.nal.usda.gov/fdc/v1/food/{fdcId}?api_key=' + API_KEY

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

    return {
        'name': json_data['description'],
        'ingredients': ingr_list,
        'nutrients': nutr_list
    }
