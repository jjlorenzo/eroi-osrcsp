
from .models import Tweet
from django.contrib import admin


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

  list_display = [
    "id",
    "created_at",
    "name",
    "message",
  ]

  list_filter = [
    "created_at",
    "name",
  ]
