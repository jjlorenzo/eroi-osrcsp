
from ..models import Tweet
from .serializers import TweetSerializer
from rest_framework import mixins
from rest_framework import viewsets


class TweetViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):

  authentication_classes = []

  queryset = Tweet.objects.all()

  serializer_class = TweetSerializer
