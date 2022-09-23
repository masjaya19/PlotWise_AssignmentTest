from django.urls import include, path
from rest_framework import routers
from myapi.views import GeoPointViewSet

router = routers.DefaultRouter()
router.register(r'geopoint', GeoPointViewSet)

urlpatterns = [
    path('', include(router.urls)),
]