from django.shortcuts import render


# Create your views here.
def homepage(request):
    context = {}

    return render(request, 'homepage.html', context=context)


# Admin pages
def admin_analytics(request):
    context = {}

    return render(request, 'admin_analytics.html', context=context)


def admin_add_user(request):
    context = {}

    return render(request, 'admin_add_user.html', context=context)


# Coach pages


# Member pages
