
from django.contrib import admin
from django.urls import path
from django.conf.urls import include


urlpatterns = [
  path("admin/", admin.site.urls),
  path("", include("osrcsp.pmtwitter.urls")),

  path("api/v1/", include(("osrcsp.pmtwitter.api.urls", "tweets"), namespace="v1")),
]
