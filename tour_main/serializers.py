from rest_framework import serializers
from .models import TourType

class TourTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourType
        fields = ('tour_id', 'name')