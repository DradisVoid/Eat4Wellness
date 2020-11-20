from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def search_food(request):
    if request.method == 'POST':
        s = request.POST['s']

        response = "<table><tbody>"

        response += "<tr><td>" + str(s) + "</td><</tr>"

        response += "</tbody></table>"

        return HttpResponse(response)
