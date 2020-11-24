from django.shortcuts import render
import requests

# Get API key from file
from .api_key import API_KEY


def get_food(fdc_id):
    if fdc_id == '':
        return {}

    url = f'https://api.nal.usda.gov/fdc/v1/food/{fdc_id}?api_key=' + API_KEY

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

    portions_list = {}
    for item in json_data['foodPortions']:
        try:
            portions_list[item['id']] = {
                'description': item['portionDescription'],
                'weight': item['gramWeight'],
            }
        except:
            pass

    return {
        'name': json_data['description'],
        'ingredients': ingr_list,
        'nutrients': nutr_list,
        'portions': portions_list
    }


def search(s):
    url = 'https://api.nal.usda.gov/fdc/v1/foods/search?api_key=' + API_KEY

    data = {
        "query": s,
        "dataType": [
            "Survey (FNDDS)"
        ]
    }

    r = requests.post(url, json=data)

    json_data = r.json()

    results = {}

    if json_data["totalHits"] > 0:
        count = 0
        for item in json_data['foods']:
            results[item['fdcId']] = {
                'name': item['description']
            }
            count += 1

    return results
