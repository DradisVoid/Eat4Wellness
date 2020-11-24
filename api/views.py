from django.shortcuts import render
import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api import api_calls


# Create your views here.
@csrf_exempt
def search_food(request):
    if request.method == 'POST':

        response = api_calls.search(request.POST.get('s', ''))

        return JsonResponse(response)
    else:
        return JsonResponse({})


@csrf_exempt
def get_food(request):
    if request.method == 'POST':

        response = api_calls.get_food(request.POST.get('id', ''))

        return JsonResponse(response)
    else:
        return JsonResponse("")
