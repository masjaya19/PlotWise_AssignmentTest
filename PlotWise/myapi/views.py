from django.shortcuts import render
from rest_framework import viewsets
from myapi.models import geopoint
from myapi.serializers import GeoPointSerializer

# Create your views here.
class GeoPointViewSet(viewsets.ModelViewSet):
   queryset = geopoint.objects.all()
   serializer_class = GeoPointSerializer
