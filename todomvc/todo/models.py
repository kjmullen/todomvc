from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    order = models.IntegerField(null=True)
