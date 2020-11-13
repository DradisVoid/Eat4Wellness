from django.shortcuts import render


# Create your views here.
def homepage(request):
    context = {}

    return render(request, 'homepage.html', context=context)


def admin_homepage(request):
    context = {}

    return render(request, 'admin_homepage.html', context=context)


def coach_homepage(request):
    context = {}

    return render(request, 'coach_homepage.html', context=context)


def member_homepage(request):
    context = {}

    return render(request, 'member_homepage.html', context=context)