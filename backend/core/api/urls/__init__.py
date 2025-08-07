from django.urls import path, include
from api.views import HealthCheckViewSet
from .accounts import urlpatterns as accounts_urls

urlpatterns = []

urlpatterns += [
   path("health/", HealthCheckViewSet.as_view({"get":"list"}), name="health_check"),
   path("auth/", include(accounts_urls)),
]
