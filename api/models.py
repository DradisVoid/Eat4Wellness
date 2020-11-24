from django.db import models


# Create your models here.
class ApiSearchCall(models.Model):
    query = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return "Search: " + self.query


class ApiGetCall(models.Model):
    fdc_id = models.PositiveIntegerField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return "Get: " + self.fdc_id
