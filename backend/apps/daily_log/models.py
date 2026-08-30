from django.db import models

from apps.authentication.models import User

# Create your models here.


class DailyLog(models.Model):
    date = models.DateTimeField(null=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="logs", null=False
    )
