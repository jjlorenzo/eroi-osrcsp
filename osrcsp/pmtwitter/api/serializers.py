
from ..models import Tweet
from rest_framework import serializers


class TweetSerializer(serializers.ModelSerializer):

  class Meta:

    fields = ("id", "name", "message", "created_at",)

    model = Tweet

    read_only_fields = ("created_at",)
