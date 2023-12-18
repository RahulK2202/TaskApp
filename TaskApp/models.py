from django.db import models
from UserApps.models import AppUsers
from django.utils.timezone import now
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    due_date = models.DateTimeField(default=now)
    user = models.ForeignKey(AppUsers, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title