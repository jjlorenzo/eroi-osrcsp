
from django.db import models
from django.utils import timezone


class Tweet(models.Model):
  name = models.CharField(max_length=20)
  message = models.CharField(max_length=50)
  created_at = models.DateTimeField(default=timezone.now)

  class Meta:
    ordering = ("created_at", "name")
