from django.db import models
from users.models import Member
from food.models import Nutrient


# Create your models here.
class HealthProfile(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=1, choices=SEX)
    member = models.OneToOneField(Member, related_name='health_profile_of', on_delete=models.CASCADE)
    average_daily_nutrients = models.ManyToManyField(Nutrient, through='HealthProfileNutrient')

    def __str__(self):
        return str(self.member) + " Health Profile"


class HealthProfileNutrient(models.Model):
    nutrient = models.ForeignKey(Nutrient, on_delete=models.CASCADE)
    health_profile = models.ForeignKey(HealthProfile, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    unit = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nutrient) + " (" + str(self.amount) + " " + self.unit + ") - Health Profile"
