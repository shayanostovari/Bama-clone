from rest_framework import serializers
from car.models import Car
from django.contrib.auth import get_user_model
User = get_user_model()


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('body', 'title', 'tip', 'color', 'model_year', 'description')
