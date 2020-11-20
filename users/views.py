from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from users.models import *
from users.forms import *


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
        pass

    form = AddMealForm()

    context = {
        'form': form
    }

    return render(request, 'member_meal_add.html', context=context)
