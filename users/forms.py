from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import User


class AddUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=150, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required.')
    is_member = forms.BooleanField(label='Is the user a member?', required=False)
    coach_id = forms.IntegerField(help_text='If user is a Member, provide their Coach', required=False)
    is_coach = forms.BooleanField(label='Is the user a coach?', required=False)
    is_admin = forms.BooleanField(label='Is the user an admin?', required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_member', 'coach_id', 'is_coach', 'is_admin',
                  'password1', 'password2',)

    def clean(self):
        data = self.cleaned_data

        if data['is_member']:
            if data['coach_id']:
                pass
            else:
                raise ValidationError("Please specify a Coach ID")

        return data


class AddMealForm(forms.Form):
    date = forms.DateTimeField(required=True, help_text='Meal Time', label='')


class AddFoodForm(forms.Form):
    food_id = forms.CharField(widget=forms.HiddenInput())
    portion_id = forms.CharField(widget=forms.HiddenInput())
    servings = forms.IntegerField(required=True)
