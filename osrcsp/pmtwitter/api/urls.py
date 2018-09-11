
from rest_framework import routers
from .viewsets import TweetViewSet


router = routers.SimpleRouter()

router.register(r"tweets", TweetViewSet)

urlpatterns = router.urls
