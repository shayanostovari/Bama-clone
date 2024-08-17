from rest_framework import serializers
from car.models import Car


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('body', 'title', 'tip', 'color', 'model_year', 'description')
