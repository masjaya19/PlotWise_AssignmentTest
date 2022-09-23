from rest_framework import serializers
from .models import geopoint

class GeoPointSerializer(serializers.ModelSerializer):


    class Meta:
        model = geopoint
        fields = ('latitude','longtitude','date')