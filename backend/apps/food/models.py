from django.db import models

from apps.daily_log.models import DailyLog

# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=200, null=False)
    calories_per_100g = models.FloatField(null=False)


class FoodEntry(models.Model):
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name="entries", null=False
    )
    daily_log = models.ForeignKey(
        DailyLog, on_delete=models.CASCADE, related_name="entries", null=False
    )
    quantity_g = models.FloatField(null=False)
